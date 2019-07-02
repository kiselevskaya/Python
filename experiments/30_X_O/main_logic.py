

import string
import random
import asyncio
import threading
from user import *
from board import *
# from board_as_class import *
# board = Board()


class MainLogic:
    def __init__(self):
        self.users = dict()
        self.started = False
        self.first = False
        self.user_info = dict()
        self.board_side = 10
        self.win_length = 5
        # self.field = None

    def add_user(self, username):
        if username in self.users:
            return None
        if 'Computer' in [*self.users] and not self.started:
            self.users.pop('Computer')
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
            self.get_connected_user_list()
            await self.send_to_all('log_off', 'user_list', [*self.users])
            if len(self.users) == 0:
                await user.disconnect()
        else:
            print("Bad connection from not exist user " + username)

    def get_connected_user_list(self):
        if len([*self.users]) == 1 and 'Computer' not in [*self.users]:
            self.add_user('Computer')
        return [*self.users]

    async def send_to_all(self, msg_name, title, content):
        data = dict()
        data['msg'] = msg_name
        data[title] = content
        await self.send_msg_to_all(data)

    async def send_msg_to_all(self, data):
        for key, user in self.users.items():
            if user != 'Computer':
                await user.send_message(data)

    async def try_start_game(self, user):
        if self.started:
            await user.send_data('cannot_start_game', 'content', "game already started")
            return False
        else:
            await self.send_to_all('start_game', 'content', "Starting the Game!")
            await self.start_countdown(3)
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
        self.started = True
        data['countdown'] = seconds
        data['started'] = True
        await self.send_msg_to_all(data)

    async def return_characters(self, char, username):
        self.started = False
        for user in [*self.users]:
            if user == username:
                await self.user_data(user, char)
            else:
                character = [ch for ch in ['X', 'O'] if ch != char][0]  # rest character after choice was made
                await self.user_data(user, character)
        await self.send_to_all('characters', 'users_data', self.user_info)

        await self.create_board(self.board_side)
        # await self.create_board(self.board_side, self.win_length)

    async def user_data(self, user, character, score=0):
        logged_off = [x for x in [*self.user_info] if x not in [*self.users]]
        if logged_off:
            self.user_info.pop(logged_off[0])

        self.first = (True if character == 'X' else False)
        self.user_info[user] = [character, score, self.first]
        return self.user_info

    # async def create_board(self, side, length):
    async def create_board(self, side):
        global board
        board = create_board(side)
        await self.send_to_all('board', 'new_board', board)
        # self.field = board.create_board(side, length)
        # await self.send_to_all('board', 'new_board', self.field)

    async def reset_board(self):
        global board
        board = [['' for y in x] for x in board]
        await self.send_to_all('board_info', 'update', board)
        # self.field = board.reset_board()
        # await self.send_to_all('board_info', 'update', self.field)

    async def process_step(self, position, username):
        self.user_info[username][2] = False  # is it turn of this user to make a step
        char = self.user_info[username][0]
        board_step(board, char, position)
        await self.send_to_all('board_info', 'update', board)
        # board.make_step(char, position[0], position[1])
        # await self.send_to_all('board_info', 'update', self.field)

        await self.check_last_step(char, position, username)

    async def process_computer_step(self, position, username=None):
        previous_pos = position
        print(previous_pos)

        steps_list = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if not board[x][y]:
                    steps_list.append([x, y])   # list of possible steps
        step = random.choice(steps_list)
        await self.process_step(step, username)

    async def check_last_step(self, char, position, username):
        steps_left = list(filter(lambda x: x == "", [lst for sublist in board for lst in sublist]))  # steps left
        # if board.check_win(char, position[0], position[1]):
        if last_step_check(board, char, position):
            await self.process_win(char, position, username)
        elif not len(steps_left):
            await self.process_draw()
        else:
            next_user = [user for user in[*self.user_info] if user != username][0]  # user who should make next step
            self.user_info[next_user][2] = True  # is it turn of this user to make a step

            if next_user == "Computer":
                await self.process_computer_step(position, next_user)

            await self.send_to_all('user_info', 'update', self.user_info)

    async def process_win(self, char, position, username):
        self.user_info[username][1] += 1    # update score
        await self.send_to_all('user_info', 'update', self.user_info)

        win_set = last_step_check(board, char, position)    # list of winning combination positions
        await self.send_to_all('winner_info', 'data', [username, win_set])

    async def process_draw(self):
        await self.send_to_all('draw', 'restart', True)

    async def process_reset(self):
        await self.reset_board()
        await self.send_to_all('reset', 'data', self.user_info)
        for user in [*self.user_info]:
            await self.user_data(user, self.user_info[user][0], self.user_info[user][1])
        await self.send_to_all('user_info', 'update', self.user_info)
