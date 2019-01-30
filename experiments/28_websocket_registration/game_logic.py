import random
import string
import websockets
import json
import traceback
import asyncio
import queue
import threading
from muppet import *


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
            return await self.process_start_game()
        if parsed_json['msg'] == 'shoot':
            return await self.process_shoot(parsed_json)
        return False

    async def process_hello(self, json_msg):
        if json_msg['username'] == self.username:
            self.connected = True
            # await self.send_user_list()
            # mock start game
            await self.game_logic.start_game()
            return True
        else:
            return False

    async def process_start_game(self):
        await self.game_logic.try_start_game(self)
        return True

    async def process_shoot(self, json_msg):
        await self.game_logic.shoot(self, json_msg["result"] == "hit")

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
                print(" -> (" + self.username + ")" + json_msg)
            try:
                await self.websocket.send(json_msg)
            except websockets.exceptions.ConnectionClosed as e:
                print(" -> ", e)
                self.websocket.close()


class GameLogic:

    def __init__(self):
        self.users = dict()
        self.game_started = False
        self.stop_the_game = False
        self.threads = []

    def add_user(self, username):
        if username in self.users:
            return None

        password = self.generate_password(username)
        user = User(username, password, self)
        self.users[username] = user

        return password

    def check_user(self, username, password):
        # mock for development {
        if username not in self.users:
            user = User(username, password, self)
            self.users[username] = user
            return True
        # mock for development }
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
            if len(self.users) == 0:
                await self.finish_game()
        else:
            print("Bad connection from not exist user " + username)

    async def send_msg_to_all(self, data):
        for key, user in self.users.items():
            await user.send_message(data)

    async def send_to_all(self, msg_name, title, content):
        data = dict()
        data['msg'] = msg_name
        data[title] = content
        await self.send_msg_to_all(data)

    async def try_start_game(self, user):
        if len(self.get_connected_user_list()) < 2:
            await user.send_data('cannot_start_game', 'content', "not enough users on server")
            return False
        elif self.game_started:
            await user.send_data('cannot_start_game', 'content', "game already started")
            return False
        else:
            self.game_started = True
            await self.send_to_all('start_game', 'content', "Starting the Game!")
            await self.start_countdown(3)
            await self.start_game()
            return True

    async def start_countdown(self, seconds):
        data = dict()
        data['msg'] = 'countdown'
        data['started'] = False
        while seconds:
            data['countdown'] = seconds
            await self.send_msg_to_all(data)
            await asyncio.sleep(1)
            seconds -= 1
        data['countdown'] = seconds
        data['started'] = True
        await self.send_msg_to_all(data)

    async def start_game(self):
        self.game_started = True
        self.stop_the_game = False

        lock = threading.Lock()

        q = queue.Queue(maxsize=0)
        num_threads = 1

        for i in range(num_threads):
            thread = threading.Thread(target=self.level_thread, args=(q, lock,))
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)

    async def finish_game(self):
        self.stop_the_game = True
        for i in self.threads:
            i.join()

    def level_thread(self, q, lock):
        print("level thread starting")
        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)
        event_loop.run_until_complete(self.async_level_thread())
        print("level thread finished")

    async def async_level_thread(self):
        print("level thread started")
        await self.send_to_all('Game Started', 'status_game', 'started')
        muppet = Muppet(muppets[0])
        while not self.stop_the_game:
            data = dict()
            data['msg'] = "tick"
            data["position"] = list([muppet.get_x(), muppet.get_y()])
            data["image"] = muppet.image

            muppet.animate()
            await asyncio.sleep(0.05)
            await self.send_msg_to_all(data)

           # lock.acquire()
           # if not q.empty:
           #     data = q.get()
           # lock.release()
           # q.task_done()

    async def shoot(self, user, hit):
        data = dict()
        if hit:
            data['msg'] = "hit"
        else:
            data['msg'] = "miss"
        data['username'] = user.username
        await self.send_msg_to_all(data)
        await self.finish_game()


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
