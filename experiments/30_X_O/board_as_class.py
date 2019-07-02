import re


class Board:
    def __init__(self, side=5, win_length=3):
        self.side = side
        self.board = []
        self.center = self.side//2
        self.win_length = win_length
        self.radius = (self.win_length*2-1)//2

    def create_board(self):
        self.board = [['' for x in range(self.side)] for y in range(self.side)]
        return self.board

    def get_field(self):
        # prints a nested list row by row as a field
        return '\n'.join([str(lst) for lst in self.board])

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def make_step(self, ch, y, x):
        self.board[x][y] = ch*(self.board[y][x] == '')
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


board = Board()
field = board.create_board()
print(repr(board))
print()
board.make_step('o', 1, 4)
board.make_step('', 2, 3)
board.make_step('x', 3, 2)
board.make_step('x', 4, 1)

board.make_step('', 0, 2)
board.make_step('', 1, 2)
board.make_step('o', 2, 2)
board.make_step('', 4, 2)

board.make_step('x', 1, 0)
board.make_step('x', 2, 1)
board.make_step('o', 4, 3)

board.make_step('x', 3, 0)
board.make_step('', 3, 1)
board.make_step('', 3, 3)
board.make_step('o', 3, 4)
print(board.get_field())
print()
board.check_win('x', 1, 2)

