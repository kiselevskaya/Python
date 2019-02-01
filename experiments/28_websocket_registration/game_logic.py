import random
import string
import asyncio
import queue
import threading
from muppet import *
from user import *


class GameLogic:

    def __init__(self):
        self.users = dict()
        self.game_started = False
        self.stop_the_game = False
        self.threads = []
        self.score = dict()
        self.lock = threading.Lock()
        self.q = asyncio.Queue(maxsize=0)

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

        num_threads = 1

        for i in range(num_threads):
            thread = threading.Thread(target=self.level_thread, args=())
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)

    async def finish_game(self):
        self.stop_the_game = True
        for i in self.threads:
            i.join()

    def level_thread(self):
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
            muppet.animate()

            await asyncio.sleep(0.1)

            self.lock.acquire()
            if not self.q.empty():
                task = self.q.get_nowait()
                user = task[0]
                msg = task[1]
                if msg["msg"] == "shoot":
                    data = dict()
                    data['username'] = user.username
                    if muppet.check_shoot(msg["result"]):
                        data['msg'] = "hit"
                    else:
                        data['msg'] = "miss"
                    await self.send_msg_to_all(data)
                self.q.task_done()
            self.lock.release()

            data = dict()
            data['msg'] = "tick"
            data["position"] = list([muppet.get_x(), muppet.get_y()])
            data["image"] = muppet.image
            await self.send_msg_to_all(data)

           # lock.acquire()
           # if not q.empty:
           #     data = q.get()
           # lock.release()
           # q.task_done()

    async def shoot(self, user, shoot_msg):
        self.lock.acquire()
        self.q.put_nowait([user, shoot_msg])
        self.lock.release()


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
