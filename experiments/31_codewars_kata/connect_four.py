

import re
import unittest


def who_is_winner(pieces_position_list):
    row_counter = {'A': 5, 'B': 5, 'C': 5, 'D': 5, 'E': 5, 'F': 5, 'G': 5}
    board = Board()
    board.create_board()
    for i in range(len(pieces_position_list)):  # ["C_Yellow", "E_Red", "G_Yellow"..."C_Red"]
        step = pieces_position_list[i]  # "C_Yellow"
        column = step.split('_')[0]  # C (A or B...G)
        who = list(step.split('_')[1])[0]  # Y (Y is Yellow or R is Red)
        y = row_counter[column]  # 5 (0-6)
        x = list(row_counter.keys()).index(column)  # 2 (0-7)
        row_counter[column] -= 1  # left {'A': 5, 'B': 5, 'C': 4, 'D': 5, 'E': 5, 'F': 5, 'G': 5}
        board.make_step(who, y, x)
        steps_counter = i+1
        if who == 'Y' and board.check_win(who, y, x, steps_counter):
            return 'Yellow'
        elif who == 'R' and board.check_win(who, y, x, steps_counter):
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
        while y+1 < self.height and x+1 < self.width and (y+1 <= y0+self.radius and x+1 <= x0+self.radius):
            y, x = y+1, x+1
            diagonally.append([self.board[y][x], [y, x]])
        # go right and up
        y, x = y0, x0
        while y-1 >= 0 and x+1 < self.width and (y-1 >= y0-self.radius and x+1 <= x0+self.radius):
            y, x = y-1, x+1
            diagonally2.insert(0, [self.board[y][x], [y, x]])
        # go left and down
        y, x = y0, x0
        while y+1 < self.height and x-1 >= 0 and (y+1 <= y0+self.radius and x-1 >= x0-self.radius):
            y, x = y+1, x-1
            diagonally2.append([self.board[y][x], [y, x]])
        return [diagonally, diagonally2]

    def check_win(self, colour, y, x, all_steps):
        if all_steps < 7:
            return
        else:
            for line in self.directions(y, x):
                txt = ''.join(map(lambda z: '0' if z == '' else z, list(line[i][0] for i in range(len(line)))))  # eg 00Y000 or 000Y or 00Y or 000Y
                try:
                    pattern = colour*self.win_length  # YYYY or RRRR
                    win_indexes = (re.search(r"{}{}*".format(pattern, colour), txt).span())
                    # print('WIN', list(line[i][1] for i in range(win_indexes[0], win_indexes[1])))
                    return True
                except AttributeError:
                    continue
        return


class TestWinner(unittest.TestCase):

    def test_win_red_1(self):
        self.assertEqual(who_is_winner([
            'B_Red', 'C_Yellow', 'D_Red', 'B_Yellow', 'G_Red', 'B_Yellow', 'A_Red', 'B_Yellow', 'F_Red', 'A_Yellow',
            'F_Red', 'E_Yellow', 'D_Red', 'G_Yellow', 'E_Red', 'D_Yellow', 'G_Red', 'C_Yellow', 'G_Red', 'C_Yellow',
            'E_Red', 'G_Yellow', 'A_Red', 'E_Yellow', 'E_Red', 'A_Yellow', 'A_Red', 'F_Yellow', 'D_Red', 'E_Yellow'
            ]), 'Red')

    def test_win_yellow_1(self):
        self.assertEqual(who_is_winner([
            'F_Red', 'E_Yellow', 'E_Red', 'D_Yellow', 'B_Red', 'F_Yellow', 'D_Red', 'E_Yellow', 'A_Red', 'G_Yellow',
            'G_Red', 'B_Yellow', 'B_Red', 'C_Yellow', 'G_Red', 'G_Yellow', 'D_Red', 'D_Yellow', 'B_Red', 'C_Yellow',
            'B_Red', 'E_Yellow', 'G_Red', 'E_Yellow', 'D_Red', 'G_Yellow'
            ]), 'Yellow')

    def test_win_red_2(self):
        self.assertEqual(who_is_winner([
            'E_Red', 'B_Yellow', 'E_Red', 'E_Yellow', 'G_Red', 'A_Yellow', 'E_Red', 'F_Yellow', 'D_Red', 'D_Yellow',
            'D_Red', 'G_Yellow', 'G_Red', 'E_Yellow', 'G_Red', 'F_Yellow', 'F_Red', 'B_Yellow', 'A_Red', 'B_Yellow',
            'B_Red', 'C_Yellow', 'B_Red', 'D_Yellow', 'D_Red', 'G_Yellow', 'C_Red', 'E_Yellow'
            ]), 'Red')

    def test_win_red_3(self):
        self.assertEqual(who_is_winner([
            'B_Red', 'A_Yellow', 'E_Red', 'D_Yellow', 'B_Red', 'D_Yellow', 'C_Red', 'E_Yellow', 'B_Red', 'F_Yellow',
            'C_Red', 'C_Yellow', 'D_Red', 'C_Yellow', 'G_Red', 'A_Yellow', 'F_Red', 'C_Yellow', 'D_Red', 'A_Yellow',
            'F_Red', 'G_Yellow', 'E_Red', 'G_Yellow', 'D_Red', 'A_Yellow', 'E_Red', 'D_Yellow'
            ]), 'Red')

    def test_win_red_4(self):
        self.assertEqual(who_is_winner([
            'G_Red', 'E_Yellow', 'E_Red', 'G_Yellow', 'B_Red', 'C_Yellow', 'D_Red', 'G_Yellow', 'F_Red', 'D_Yellow',
            'A_Red', 'D_Yellow', 'A_Red', 'C_Yellow', 'D_Red', 'D_Yellow', 'G_Red', 'B_Yellow', 'A_Red', 'F_Yellow',
            'F_Red', 'B_Yellow', 'B_Red', 'G_Yellow', 'E_Red', 'C_Yellow', 'B_Red', 'F_Yellow', 'F_Red', 'F_Yellow'
            ]), 'Red')

    def test_win_red_5(self):
        self.assertEqual(who_is_winner([
            'G_Red', 'G_Yellow', 'D_Red', 'B_Yellow', 'B_Red', 'B_Yellow', 'E_Red', 'B_Yellow', 'A_Red', 'C_Yellow',
            'D_Red', 'D_Yellow', 'E_Red', 'F_Yellow', 'F_Red', 'G_Yellow', 'G_Red', 'B_Yellow', 'A_Red', 'G_Yellow',
            'E_Red', 'C_Yellow', 'F_Red', 'D_Yellow', 'D_Red', 'F_Yellow', 'C_Red', 'C_Yellow', 'A_Red', 'C_Yellow',
            'G_Red'
            ]), 'Red')

    def test_win_yellow_2(self):
        self.assertEqual(who_is_winner([
            "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
            "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
            "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
            ]), 'Yellow')

    def test_win_yellow_3(self):
        self.assertEqual(who_is_winner([
            "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
            "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
            "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
            "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
            "E_Yellow", "E_Red"
            ]), 'Yellow')

    def test_win_red_6(self):
        self.assertEqual(who_is_winner([
            "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
            "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
            "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
            "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
            "B_Yellow", "B_Red"
            ]), 'Red')

    def test_win_red_7(self):
        self.assertEqual(who_is_winner([
            "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
            "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
            ]), 'Red')

    def test_win_yellow_4(self):
        self.assertEqual(who_is_winner([
            "A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
            ]), 'Yellow')

    def test_win_draw(self):
        self.assertEqual(who_is_winner([
            "A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
            ]), 'Draw')


if __name__ == '__main__':
    unittest.main()
