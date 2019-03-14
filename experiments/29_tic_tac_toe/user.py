

import websockets
import json
import traceback


class User:
    def __init__(self, username, password, main_logic):
        self.username = username
        self.password = password
        self.main_logic = main_logic
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
        if parsed_json['msg'] == 'choice':
            return await self.process_choice(parsed_json)
        if parsed_json['msg'] == 'step':
            return await self.process_step(parsed_json)
        return False

    async def process_hello(self, json_msg):
        if json_msg['username'] == self.username:
            self.connected = True
            await self.send_user_list()
            return True
        else:
            return False

    async def process_choice(self, json_msg):
        await self.main_logic.start_game(json_msg)
        return True

    async def process_step(self, json_msg):
        await self.main_logic.next_step(json_msg)
        return True

    async def send_user_list(self):
        user_list = self.main_logic.get_connected_user_list()
        await self.main_logic.send_to_all('user_list', 'user_list', list(user_list))

    async def send_message(self, msg):
        if self.connected:
            json_msg = json.dumps(msg)
            if msg["msg"] == "user_list":
                print(" -> (" + self.username + ")" + json_msg)
            try:
                await self.websocket.send(json_msg)
            except websockets.exceptions.ConnectionClosed as e:
                print(" -> ", e)
                await self.websocket.close()

    async def disconnect(self):
        self.gracefully_disconnected = True
        await self.websocket.close()
