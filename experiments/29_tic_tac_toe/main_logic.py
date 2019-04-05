

import string
import random
import asyncio
import threading
from user import *
from board import *


class MainLogic:
    def __init__(self):
        self.users = dict()
        self.started = False

    def add_user(self, username):
        if username in self.users:
            return None
        if len(self.users) < 2 and not self.started:
            password = self.generate_password(username)
            user = User(username, password, self)
            self.users[username] = user
            return password
        else:
            return None

    @staticmethod
    def generate_password(username):
        return username + ''.join(random.choices(string.ascii_uppercase + string.digits, k=40))

    def check_user(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password and user.connected is not True:
                return True
        return False

    async def process_websocket(self, username, websocket):
        if username in self.users:
            user = self.users[username]
            await user.process_websocket(websocket)
            self.users.pop(username)
            if len(self.users) == 0:
                await user.disconnect()
        else:
            print("Bad connection from not exist user " + username)

    def get_connected_user_list(self):
        res = []
        for k, v in self.users.items():
            if v.connected:
                res.append(k)
        return res

    async def send_to_all(self, msg_name, title, content):
        data = dict()
        data['msg'] = msg_name
        data[title] = content
        await self.send_msg_to_all(data)

    async def send_msg_to_all(self, data):
        for key, user in self.users.items():
            await user.send_message(data)

    async def start_game(self, msg):
        global board
        self.started = msg['status']
        board = create_board(5)
        await self.send_to_all('board', 'new_board', board)

    async def next_step(self, msg):
        lst = []
        pos = msg['position']
        char = msg['char']
        board_step(board, char, pos)
        if last_step_check(board, char, pos):
            win_combination = last_step_check(board, char, pos)
            print(win_combination)
            await self.send_to_all('win', 'combination', win_combination)
        for i in board:
            for e in i:
                if e == '':
                    lst.append(e)
        if len(lst) > 0 and len([*self.users]) == 1:
            next_player = 'Computer'
            await self.send_to_all('next', 'next_player', next_player)
        else:
            await self.send_to_all('stop', 'draw', True)

    async def restart_board(self, msg):
        await self.start_game(msg)
