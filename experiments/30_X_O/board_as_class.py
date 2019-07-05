

from patterns import *
import re


pattern = Patterns()
compare_with = pattern.get_patterns()

class Board:
    def __init__(self, side=5, win_length=3):
        self.side = side
        self.board = []
        self.center = self.side//2
        self.win_length = win_length
        self.radius = (self.win_length*2-1)//2
        self.potential_steps = []

    def create_board(self):
        self.board = [['' for x in range(self.side)] for y in range(self.side)]
        return self.board

    def get_field(self):
        # prints a nested list row by row as a field
        return '\n'.join([str(lst) for lst in self.board])

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def make_step(self, ch, y, x):
        self.board[y][x] = ch*(self.board[y][x] == '')
        return self.board

    def reset_board(self):
        self.board = [['' for x in y] for y in self.board]
        return self.board

    def directions(self, y=None, x=None):
        row = list(i for i in range(y-self.radius, (y+self.radius)+1) if 0 <= i < self.side)
        column = list(i for i in range(x-self.radius, (x+self.radius)+1) if 0 <= i < self.side)
        horizontal = list([self.board[y][u], [y, u]] for u in column)
        vertical = list([self.board[v][x], [v, x]] for v in row)
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

    def check_win(self, ch, y, x):
        for line in self.directions(y, x):
            print(line)
            txt = ''.join(map(lambda z: '0' if z == '' else z, list(line[i][0] for i in range(len(line)))))
            try:
                pattern = ch*self.win_length
                win_indexes = (re.search(r"{}{}*".format(pattern, ch), txt).span())
                print('WIN', list(line[i][1] for i in range(win_indexes[0], win_indexes[1])))
                return list(line[i][1] for i in range(win_indexes[0], win_indexes[1]))
            except AttributeError:
                continue
        return False

    def get_possibilities(self, ch, y, x):
        for line in self.directions(y, x):
            self.potential_steps += (list(line[i][1] for i in range(len(line)) if line[i][0] == ''))
        try:
            self.potential_steps.pop(self.potential_steps.index([y, x]))
        except ValueError:
            print('Not in list')
        print(self.potential_steps)

    def get_value(self):
        check_pattern, result = [], [[], []]
        # check by example just on first possible step in all which are in potential steps list
        for j in range(len(self.potential_steps)):
            y = self.potential_steps[j][0]
            x = self.potential_steps[j][1]
            for line in self.directions(y, x):
                indx = [i for i in range(len(line)) if line[i][1] == [y, x]][0]
                line[indx][0] = '7'
                txt = ''.join(map(lambda x: '0' if x == '' else x, list(line[i][0] for i in range(len(line)))))
                txt = re.sub('[x]', '1', txt)
                txt = re.sub('[o]', '2', txt)
                check_pattern.append(txt)
                print('Compare this with patterns to get value', check_pattern)
                for i in range(len(self.compare_patterns(txt, y, x))):
                    if len(self.compare_patterns(txt, y, x)[i]) != 0:
                        result[i] += self.compare_patterns(txt, y, x)[i]
        print(result)
        # if no math:
        # if (y <=1 and x <= 1) or (y >= len(self.board)-2 and x >= len(self.board)-2): value = 3
        # elif y*x == 0 or y = -x or x == -y: value = 2
        # else: value = 1
        return result

    def compare_patterns(self, txt, y, x):
        x_value, o_value = [], []
        for i in range(len(compare_with[1])):
            if re.match(compare_with[1][i], txt):
                print(re.match(compare_with[1][i], txt))
                print('value: {}, pos: {}, pattern: {}'.format(compare_with[0][i], [y, x], compare_with[1][i]))
                x_value.append([compare_with[0][i], [y, x]])
            elif re.match(compare_with[2][i], txt):
                print(re.match(compare_with[2][i], txt))
                print('value: {}, pos: {}, pattern: {}'.format(compare_with[0][i], [y, x], compare_with[2][i]))
                o_value.append([compare_with[0][i], [y, x]])
        return [x_value, o_value]


board = Board()


class Computer:
    def __init__(self, ch='x'):
        self.attack = []
        self.defense = []
        self.y = board.center
        self.x = board.center
        self.ch = ch
        self.defense = []
        self.attack = []

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def make_step(self, y=None, x=None, ch=None):
        if ch or y or x is not None: self.ch, self.y, self.x = ch, y, x
        board.make_step(self.ch, self.y, self.x)

    def step_analise(self):
        # should compare patterns and return position to make best step
        board.get_possibilities(self.ch, self.y, self.x)


field = board.create_board()

ai = Computer()
ai.make_step()
print(board.get_field())
ai.step_analise()
print()

board.make_step('x', 1, 2)
board.make_step('o', 2, 1)
print(board.get_field())
board.get_possibilities('o', 2, 1)
print()
print(board.get_value())
