import random
import string
import websockets
import json
import traceback
import asyncio
import math


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
        return False

    async def process_hello(self, json_msg):
        if json_msg['username'] == self.username:
            self.connected = True
            await self.send_user_list()
            return True
        else:
            return False

    async def process_start_game(self):
        await self.game_logic.try_start_game(self)
        return True

    # async def process_game_in_progress(self):
    #     if len(self.game_logic.get_connected_user_list()) < 2:
    #         await self.send_data('game_stopped', 'content', "not enough users on server")
    #         return True
    #     else:
    #         await self.send_data('not_finished', 'content', "Game in progress, wait until it'll be finished!")
    #         print("Game in progress, wait until it'll be finished!!!!")
    #         return True

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

    async def send_msg_to_all(self, data):
        for key, user in self.users.items():
            await user.send_message(data)

    async def send_to_all(self, msg, title, content):
        data = dict()
        data['msg'] = msg
        data[title] = content
        for key, user in self.users.items():
            await user.send_message(data)

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
            print("STARTING GAME!!!!")
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


class Muppet:
    def __init__(self, image, image_size=50, width=600, height=600, step=60):
        self.image = image
        self.image_size = image_size
        self.width = width
        self.height = height
        self.center = [self.width/2 - self.image_size/2, self.height/2 - self.image_size/2]
        self.pos = [self.center[0], self.center[1]]
        self.step = step
        self.increment = 2*math.pi/self.step
        self.theta = self.increment
        self.decrease = False
        self.graph = [[self.theta * math.cos(self.theta)], [self.theta * math.sin(self.theta)]]

    def __str__(self):
        return '{}, {}, {}'.format(self.pos[0], self.pos[1], self.image)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def animate(self):
        xy = self.process_direction(self.pos[0], self.pos[1], self.graph[0], self.graph[1])
        # vel = 5*(muppets.index(self.image)+1)
        vel = 30
        self.pos[0] = self.center[0] + xy[0]*vel
        self.pos[1] = self.center[1] + xy[1]*vel
        return self

    def process_direction(self, old_x, old_y, move_x, move_y):
        half_img = self.image/2

        if (move_x > self.center[0] + self.width/2 - half_img or
                move_y > self.center[1] + self.height/2 - half_img or
                move_x < self.center[0] - self.width/2 + half_img or
                move_y < self.center[1] - self.height/2 + half_img and
                not self.decrease):
            self.decrease = True
        elif old_x == self.center[0] and old_y == self.center[1]:
            self.decrease = False

        if self.decrease:
            self.theta -= self.increment
        else:
            self.theta += self.increment

        x = move_x
        y = move_y
        return [x, y]


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
