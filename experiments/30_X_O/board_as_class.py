import re


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
        # all positions in row, column
        ys = list(i for i in range(y-self.radius, (y+self.radius)+1) if 0 <= i < self.side)
        xs = list(i for i in range(x-self.radius, (x+self.radius)+1) if 0 <= i < self.side)

        horizontal = list([self.board[y][u], [y, u]] for u in xs)
        vertical = list([self.board[v][x], [v, x]] for v in ys)
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
            txt = ''.join(map(lambda x: '0' if x == '' else x, list(line[i][0] for i in range(len(line)))))
            try:
                pattern = ch*self.win_length
                win_indexes = (re.search(r"{}{}*".format(pattern, ch), txt).span())
                print('WIN', list(line[i][1] for i in range(win_indexes[0], win_indexes[1])))
                return list(line[i][1] for i in range(win_indexes[0], win_indexes[1]))
            except AttributeError:
                continue

    def get_possibilities(self, ch, y, x):
        for line in self.directions(y, x):
            txt = ''.join(map(lambda x: '0' if x == '' else x, list(line[i][0] for i in range(len(line)))))
            d = re.sub('[x]', '1', txt)
            d = re.sub('[o]', '2', d)
            print(d, (list(line[i][1] for i in range(len(line)) if line[i][0] == '')))
            self.potential_steps += (list(line[i][1] for i in range(len(line)) if line[i][0] == ''))
            # try:
            #     # output = re.search(r"[^o]{5}[^o]*", txt).span() if ch == 'x' else re.search(r"[^x]{5}[^x]*", txt).span()
            #     if ch == 'x':
            #         pos_idx = re.search(r"[^o]{5}[^o]*", txt).span()
            #         quantity = len(re.findall(r'[x]', txt))
            #     else:
            #         pos_idx = re.search(r"[^x]{5}[^x]*", txt).span()
            #         quantity = len(re.findall(r'[o]', txt))
            #     print(txt, pos_idx)
            #     possible_steps = list(line[i][1] for i in range(len(line)))
            #     print(possible_steps)
            # except AttributeError:
            #     continue
        print(self.potential_steps)

    # def get_comparison(self, txt, line):
    #     empty_steps = []
    #     for i in range(len(line)):
    #         if line[i][0] == 0:
    #             empty_steps.append(line[i][1])
    #     print(empty_steps)
    #     return empty_steps

    def get_value(self):
        # check just on first possible step in all which are in potential steps list
        # 1. get directions
        check_pattern = []
        y = self.potential_steps[0][0]
        x = self.potential_steps[0][1]
        for line in self.directions(y, x):
            txt = ''.join(map(lambda x: '0' if x == '' else x, list(line[i][0] for i in range(len(line)))))
            txt = re.sub('[x]', '1', txt)
            txt = re.sub('[o]', '2', txt)
            check_pattern.append(txt)
        check_pattern = '|'.join(check_pattern)
        print('Compare this with patterns to get value', check_pattern)
        # if no math:
        # if (y <=1 and x <= 1) or (y >= len(self.board)-2 and x >= len(self.board)-2): value = 3
        # elif y*x == 0 or y = -x or x == -y: value = 2
        # else: value = 1
        return check_pattern


board = Board()


class Computer:
    def __init__(self, ch='x'):
        self.attack = []
        self.defense = []
        self.y = board.center
        self.x = board.center
        self.ch = ch

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def make_step(self, ch=None, y=None, x=None):
        if ch or y or x is not None: self.ch, self.y, self.x = ch, y, x
        board.make_step(self.ch, self.y, self.x)

    def step_analise(self):
        board.get_possibilities(self.ch, self.y, self.x)


field = board.create_board()
print(repr(board))
print(board.get_field())
print()

ai = Computer()
ai.make_step()
print(board.get_field())
ai.step_analise()
print()

board.make_step('o', 2, 1)
print(board.get_field())
board.get_possibilities('o', 2, 1)
# board.make_step('', 2, 3)
# board.make_step('o', 3, 2)
# board.make_step('o', 4, 1)
#
# board.make_step('', 0, 2)
# board.make_step('', 1, 2)
# board.make_step('', 4, 2)
#
# board.make_step('o', 1, 0)
# board.make_step('x', 2, 1)
# board.make_step('o', 4, 3)
#
# board.make_step('o', 3, 0)
# board.make_step('', 3, 1)
# board.make_step('', 3, 3)
# board.make_step('o', 3, 4)
print()
print(board.get_value())

