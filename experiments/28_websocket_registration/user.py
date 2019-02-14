

import websockets
import json
import traceback


class User:
    def __init__(self, username, password, game_logic):
        self.username = username
        self.password = password
        self.game_logic = game_logic
        self.websocket = None
        self.connected = False
        self.gracefully_disconnected = False

    async def process_websocket(self, websocket):
        self.websocket = websocket
        print("starting processing " + self.username)
        while True:
            try:
                msg = await websocket.recv()
                print("user income msg "+str(msg))
                correct = await self.process_income_message(msg)
                if not correct:
                    await self.websocket.close()
                    break
            except websockets.exceptions.ConnectionClosed as e:
                if not self.gracefully_disconnected:
                    traceback.print_exc()
                break
            except json.decoder.JSONDecodeError as e:
                traceback.print_exc()
                break
            except TypeError as e:
                traceback.print_exc()
                break
        self.connected = False
        await self.send_user_list()
        self.websocket = None

    async def process_income_message(self, msg):
        parsed_json = json.loads(msg)
        print(" <- (" + self.username + ")" + msg)
        if parsed_json['msg'] == 'hello':
            return await self.process_hello(parsed_json)
        if parsed_json['msg'] == 'start_game':
            return await self.process_start_game()
        if parsed_json['msg'] == 'shoot':
            return await self.process_shoot(parsed_json)
        return False

    async def process_hello(self, json_msg):
        if json_msg['username'] == self.username:
            self.connected = True
            await self.send_user_list()
            # mock start game
            # await self.game_logic.start_game()
            return True
        else:
            return False

    async def process_start_game(self):
        await self.game_logic.try_start_game(self)
        return True

    async def process_shoot(self, json_msg):
        await self.game_logic.shoot(self, json_msg)
        return True

    #
    async def send_user_list(self):
        user_list = self.game_logic.get_connected_user_list()
        # await self.send_data('user_list', 'user_list', list(user_list))
        await self.game_logic.send_to_all('user_list', 'user_list', list(user_list))

    async def send_data(self, msg, title, content):
        data = dict()
        data['msg'] = msg
        data[title] = content
        await self.send_message(data)

    async def send_message(self, msg):
        if self.connected:
            json_msg = json.dumps(msg)
            if msg["msg"] != "tick":
                if msg["msg"] != "hit" or msg["msg"] != "miss":
                    print(" -> (" + self.username + ")" + json_msg)
            try:
                await self.websocket.send(json_msg)
            except websockets.exceptions.ConnectionClosed as e:
                print(" -> ", e)
                await self.websocket.close()

    async def disconnect(self):
        self.gracefully_disconnected = True
        await self.websocket.close()
