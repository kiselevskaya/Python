import random
import string
import asyncio
import threading
import time
from muppet import *
from user import *
from round import *


end_images = ['won.png', 'game_over.png']


class GameLogic:

    def __init__(self):
        self.users = dict()
        self.game_started = False
        self.stop_the_game = False
        self.threads = []
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
        # if username not in self.users:
        #     user = User(username, password, self)
        #     self.users[username] = user
        #     return True
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
        # if len(self.get_connected_user_list()) < 2:
        #     await user.send_data('cannot_start_game', 'content', "not enough users on server")
        #     return False
        if self.game_started:
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

        # num_threads = 1

        asyncio.ensure_future(self.async_level_thread())

        # for i in range(num_threads):
        #     thread = threading.Thread(target=self.level_thread, args=(asyncio.get_event_loop(),))
        #     thread.setDaemon(True)
        #     thread.start()
        #     self.threads.append(thread)

    async def finish_game(self):
        await self.finish_after(3)
        self.stop_the_game = True
        self.game_started = False
        stop_game = dict()
        stop_game['msg'] = "stop"
        stop_game['status'] = True
        await self.send_msg_to_all(stop_game)
        for i in self.threads:
            i.join()
        print("check>>", self.users)

    async def finish_after(self, delay):
        await asyncio.sleep(delay)
        return

    def level_thread(self, event_loop):
        print("level thread starting")
        event_loop.run_until_complete(self.async_level_thread())
        print("level thread finished")

    async def async_level_thread(self):
        print("level thread started")
        muppet = Muppet(muppets[0])
        round = Round(muppet.image)
        losers = 0
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
                        if round.hit(user.username):
                            await self.send_msg_to_all(data)
                            if round.win(user.username):
                                await self.win_msg(user.username)
                                # await user.disconnect()
                                await self.finish_game()
                            else:
                                await self.change_level(muppet, round)
                    else:
                        data['msg'] = "miss"
                        await self.send_msg_to_all(data)
                        if round.miss(user.username):
                            await self.lost_msg(user.username)
                            losers += 1
                            if losers == len([*self.users]):
                                await self.finish_game()
                            # await user.disconnect()
                    # await self.send_msg_to_all(data)
                self.q.task_done()
            self.lock.release()

            if not self.stop_the_game:
                data = dict()
                data['msg'] = "tick"
                data["position"] = list([muppet.get_x(), muppet.get_y()])
                data["image"] = muppet.image
                await self.send_msg_to_all(data)

    async def shoot(self, user, shoot_msg):
        self.lock.acquire()
        self.q.put_nowait([user, shoot_msg])
        self.lock.release()

    async def change_level(self, muppet, round):
        muppet.change_image()
        level_round = dict()
        level_round['msg'] = "round"
        level_round['level'] = round.level
        await self.send_msg_to_all(level_round)

    async def win_msg(self, username):
        win = dict()
        win['msg'] = "win"
        win['username'] = username
        win['image'] = end_images[0]
        await self.send_msg_to_all(win)
        for user in [*self.users]:
            if user != username:
                await self.lost_msg(user)

    async def lost_msg(self, username):
        lost_round = dict()
        lost_round['msg'] = "lost"
        lost_round['username'] = username
        lost_round['image'] = end_images[1]
        await self.send_msg_to_all(lost_round)


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
