import random
import string
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

    async def process_websocket(self, websocket):
        self.websocket = websocket
        print("starting processing " + self.username)
        while True:
            try:
                msg = await websocket.recv()
                correct = await self.process_income_message(msg)
                if not correct:
                    await self.websocket.close()
                    break
            except websockets.exceptions.ConnectionClosed as e:
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
            if not self.game_logic.game_started:
                return await self.process_start_game(parsed_json)
            else:
                return await self.process_game_in_progress()
        return False

    async def process_hello(self, json_msg):
        if json_msg['username'] == self.username:
            self.connected = True
            await self.send_user_list()
            return True
        else:
            return False

    async def process_start_game(self, parsed_json):
        if len(self.game_logic.get_connected_user_list()) < 2:
            data = dict()
            data['msg'] = 'cannot_start_game'
            data['content'] = "not enough users on server"
            await self.send_message(data)
            return True
        else:
            self.game_logic.game_started = True
            data = dict()
            data['msg'] = 'start_game'
            data['content'] = "Game was started!"
            await self.game_logic.send_to_all(data)
            await self.game_logic.countdown(10)
            print("STARTING GAME!!!!")
            return True

    async def process_game_in_progress(self):
        if len(self.game_logic.get_connected_user_list()) < 2:
            data = dict()
            data['msg'] = 'game_stopped'
            data['content'] = "not enough users on server"
            await self.send_message(data)
            return True
        else:
            data = dict()
            data['msg'] = 'not_finished'
            data['content'] = "Game in progress, wait until it'll be finished!"
            await self.send_message(data)
            print("Game in progress, wait until it'll be finished!!!!")
            return True

    async def send_user_list(self):
        user_list = self.game_logic.get_connected_user_list()
        data = dict()
        data['msg'] = 'user_list'
        data['user_list'] = list(user_list)
        await self.game_logic.send_to_all(data)

    async def send_message(self, msg):
        if self.connected:
            json_msg = json.dumps(msg)
            print(" -> (" + self.username + ")" + json_msg)
            await self.websocket.send(json_msg)


class GameLogic:

    def __init__(self):
        self.users = dict()
        self.game_started = False

    def add_user(self, username):
        if username in self.users:
            return None

        password = self.generate_password(username)
        user = User(username, password, self)
        self.users[username] = user

        return password

    def check_user(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password and user.connected is not True:
                return True
        return False

    def get_connected_user_list(self):
        res = []
        for k, v in self.users.items():
            if v.connected:
                res.append(k)
        return res

    @staticmethod
    def generate_password(username):
        return username + ''.join(random.choices(string.ascii_uppercase + string.digits, k=40))

    async def process_websocket(self, username, websocket):
        if username in self.users:
            user = self.users[username]
            await user.process_websocket(websocket)
            self.users.pop(username)

    async def send_to_all(self, msg):
        for key, user in self.users.items():
            await user.send_message(msg)

    async def countdown(self, seconds):
        import time
        data = dict()
        data['msg'] = 'countdown'
        while seconds:
            mins, secs = divmod(seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            data['countdown'] = timeformat
            await self.send_to_all(data)
            time.sleep(1)
            seconds -= 1
        data['countdown'] = '\nSTART!\n'
        await self.send_to_all(data)


if __name__ == '__main__':
    import unittest

    class GameLogicTest(unittest.TestCase):
        def testAddUser(self):
            game_logic = GameLogic()
            self.assertIsNotNone(game_logic.add_user("Bobrick"))
            self.assertIsNone(game_logic.add_user("Bobrick"))
            self.assertIsNotNone(game_logic.add_user("Lasto"))
            self.assertIsNone(game_logic.add_user("Lasto"))

        def testCheckUser(self):
            game_logic = GameLogic()
            password = game_logic.add_user("Bobrick")
            self.assertTrue(game_logic.check_user("Bobrick", password))
            self.assertFalse(game_logic.check_user("Bobrick", "D" + password))
            self.assertFalse(game_logic.check_user("Bobrick", ""))

    unittest.main()
