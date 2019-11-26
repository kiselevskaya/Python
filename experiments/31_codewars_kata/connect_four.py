

import re


def who_is_winner(pieces_position_list):
    row_counter = {'A': 5, 'B': 5, 'C': 5, 'D': 5, 'E': 5, 'F': 5, 'G': 5}
    steps_counter = 0
    board = Board()
    board.create_board()
    for i in range(len(pieces_position_list)):
        step = pieces_position_list[i]
        steps_counter += 1
        column = step.split('_')[0]
        who = list(step.split('_')[1])[0]
        y = row_counter[column]
        x = list(row_counter.keys()).index(column)
        row_counter[column] -= 1
        board.make_step(who, y, x)
        if board.check_win(who, y, x, steps_counter) == 'Y':
            return 'Yellow'
        elif board.check_win(who, y, x, steps_counter) == 'R':
            return 'Red'
    return 'Draw'


class Board:
    def __init__(self, width=7, height=6, win_length=4):
        self.width = width
        self.height = height
        self.board = []
        self.win_length = win_length
        self.radius = (self.win_length*2-1)//2

    def create_board(self):
        self.board = [['' for x in range(self.width)] for y in range(self.height)]
        return self.board

    def get_field(self):
        # draw the field
        return '\n'.join([str(lst) for lst in self.board])

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def make_step(self, colour, y, x):
        self.board[y][x] = colour
        return self.board

    def directions(self, y, x):
        row = list(i for i in range(x-self.radius, (x+self.radius)+1) if 0 <= i < self.width)
        column = list(i for i in range(y-self.radius, (y+self.radius)+1) if 0 <= i < self.height)
        horizontal = list([self.board[y][u], [y, u]] for u in row)
        vertical = list([self.board[v][x], [v, x]] for v in column)
        # each line contains a nested list with elements of character and position eg. [['x', [3, 2]],...]
        output = [horizontal, vertical]+self.get_diagonals(y, x)
        return output

    def get_diagonals(self, y, x):
        diagonally = [[self.board[y][x], [y, x]]]
        diagonally2 = [[self.board[y][x], [y, x]]]
        y0, x0 = y, x
        # go left and up
        while y-1 >= 0 and x-1 >= 0 and (y-1 >= y0-self.radius and x-1 >= x0-self.radius):
            y, x = y-1, x-1
            diagonally.insert(0, [self.board[y][x], [y, x]])
        # go right and down
        y, x = y0, x0
        while y+1 < len(self.board) and x+1 < len(self.board) and (y+1 <= y0+self.radius and x+1 <= x0+self.radius):
            y, x = y+1, x+1
            diagonally.append([self.board[y][x], [y, x]])
        # go right and up
        y, x = y0, x0
        while y-1 >= 0 and x+1 < len(self.board) and (y-1 >= y0-self.radius and x+1 <= x0+self.radius):
            y, x = y-1, x+1
            diagonally2.insert(0, [self.board[y][x], [y, x]])
        # go left and down
        y, x = y0, x0
        while y+1 < len(self.board) and x-1 >= 0 and (y+1 <= y0+self.radius and x-1 >= x0-self.radius):
            y, x = y+1, x-1
            diagonally2.append([self.board[y][x], [y, x]])
        return [diagonally, diagonally2]

    def check_win(self, colour, y, x, all_steps):
        if all_steps < 7:
            return
        else:
            for line in self.directions(y, x):
                txt = ''.join(map(lambda z: '0' if z == '' else z, list(line[i][0] for i in range(len(line)))))
                try:
                    pattern = colour*self.win_length
                    win_indexes = (re.search(r"{}{}*".format(pattern, colour), txt).span())
                    return colour
                except AttributeError:
                    continue
        return


print(who_is_winner([
    "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
    "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
    "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
    ]))   # 'Yellow'

print(who_is_winner([
    "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
    "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
    "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
    "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
    "E_Yellow", "E_Red"
    ]))   # 'Yellow'

print(who_is_winner([
    "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
    "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
    "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
    "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
    "B_Yellow", "B_Red"
    ]))    # 'Red'

print(who_is_winner([
    "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
    "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
    ]))    # 'Red'

print(who_is_winner([
    "A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
    ]))    # 'Yellow'

print(who_is_winner([
    "A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
    ]))    # 'Draw'
