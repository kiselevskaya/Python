

import string
import random
import asyncio
import threading
from user import *
from board import *


class MainLogic:
    def __init__(self):
        self.users = dict()
        self.game_started = False
        self.stop_the_game = False
        self.first = False
        self.user_info = dict()

    def add_user(self, username):
        if username in self.users:
            return None
        if len(self.users) < 2:
            password = self.generate_password(username)
            user = User(username, password, self)
            self.users[username] = user
            return password

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
        return [*self.users]

    async def send_to_all(self, msg_name, title, content):
        data = dict()
        data['msg'] = msg_name
        data[title] = content
        await self.send_msg_to_all(data)

    async def send_msg_to_all(self, data):
        for key, user in self.users.items():
            await user.send_message(data)

    async def try_start_game(self, user):
        if self.game_started:
            await user.send_data('cannot_start_game', 'content', "game already started")
            return False
        else:
            await self.send_to_all('start_game', 'content', "Starting the Game!")
            await self.start_countdown(1)
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

    async def return_characters(self, char, username):
        for user in [*self.users]:
            if user == username:
                await self.check_first_player(char)
                self.user_info[user] = [char, 0, self.first]
            else:
                character = [ch for ch in ['X', 'O'] if ch != char][0]
                await self.check_first_player(character)
                self.user_info[user] = [character, 0, self.first]

        await self.send_to_all('characters', 'users_data', self.user_info)

        await self.create_board(10)

    async def check_first_player(self, character):
        if character == 'X':
            self.first = True
        else:
            self.first = False
        return self.first

    async def create_board(self, side):
        global board
        board = create_board(side)
        await self.send_to_all('board', 'new_board', board)

    async def process_step(self, position, username):
        self.user_info[username][2] = False
        char = self.user_info[username][0]
        board_step(board, char, position)
        await self.send_to_all('board_info', 'update', board)

        await self.check_last_step(char, position, username)

    async def check_last_step(self, char, position, username):
        if last_step_check(board, char, position):
            self.user_info[username][1] += 1
            await self.send_to_all('user_info', 'update', self.user_info)
            win_set = last_step_check(board, char, position)
            await self.send_to_all('winner_info', 'data', [username, win_set])
        else:
            next_user = [user for user in[*self.user_info] if user != username]
            self.user_info[next_user[0]][2] = True
            await self.send_to_all('user_info', 'update', self.user_info)
