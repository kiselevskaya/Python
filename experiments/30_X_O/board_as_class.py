

class Board:
    def __init__(self, side=15, win_length=5):
        self.side = side
        self.board = []
        self.center = self.side//2
        self.win_length = win_length
        self.radius = (self.win_length*2-1)//2

    def create_board(self):
        self.board = [['' for y in range(self.side)] for x in range(self.side)]
        return self.board

    def get_field(self):
        # prints a nested list row by row as a field
        return '\n'.join([str(lst) for lst in self.board])

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def make_step(self, ch='x', x=7, y=7):
        self.board[x][y] = ch*(self.board[x][y] == '')
        return self.board

    def get_possibilities(self, x=None, y=None):
        # all positions in row, column or diagonals in certain radius
        xs = list(i for i in range(x-self.radius, (x+self.radius)+1) if 0 <= i < self.side)
        ys = list(i for i in range(y-self.radius, (y+self.radius)+1) if 0 <= i < self.side)
        dxy1 = list(zip(xs, ys))
        dxy2 = list(zip(xs, ys[::-1]))

        horizontal = []
        vertical = []
        diagonally = []
        diagonally2 = []
        for u in ys:
            horizontal.append([self.board[x][u], [x, u]])
        for v in xs:
            vertical.append([self.board[v][y], [v, y]])
        for i in dxy1:
            diagonally.append([self.board[i[0]][i[1]], [i[0], i[1]]])
        for i in dxy2:
            diagonally2.append([self.board[i[0]][i[1]], [i[0], i[1]]])

        # each line contains a nested list with elements of character and position eg. [['x', [3, 2]],...]
        return [horizontal, vertical, diagonally, diagonally2]

    def get_check_line(self, line=None):
        # returns string of characters in the checking line to further comparison with patterns
        # return ''.join(map(lambda x: '0' if x == '' else x, list(line[i][0] for i in range(len(line)))))
        return ''.join(map(lambda x: '0' if x == '' else 'x', list(line[i][0] for i in range(len(line)))))

    def best_lines(self, x=None, y=None, patterns=None, ch=None):
        all_best = []
        for line in self.get_possibilities(x, y):
            all_best.append(self.max_line_value(self.get_check_line(line), patterns)*(not 0))
        # get index of max val in all best which will be the index of line in self.get_possibilities
        # so could be extracted line of positions for best step
        return all_best

    def max_line_value(self, check_line, patterns=None):
        all_match = []
        for pattern in patterns:
            try:
                ''.join(check_line).index(''.join(pattern['pattern']))
                all_match.append(pattern)
            except ValueError:
                continue
        try:
            return list(p for p in patterns if p['value'] == max(list(i['value'] for i in all_match)))
        except ValueError:
            return False


pre_patterns = [{'value': 10000, 'pattern': ['xxxxx']},
                {'value': 1000, 'pattern': ['0xxxx0']},
                {'value': 500, 'pattern': ['xxxx0']},
                {'value': 400, 'pattern': ['x0xxx', 'xx0xx']},
                {'value': 100, 'pattern': ['00xxx000']},
                {'value': 80, 'pattern': ['00xxx00']},
                {'value': 75, 'pattern': ['0xxx00']},
                {'value': 50, 'pattern': ['0xxx0', 'xxx00']},
                {'value': 25, 'pattern': ['x0xx0', 'xx0x0', 'x00xx']},
                {'value': 10, 'pattern': ['000xx000']},
                {'value': 5, 'pattern': ['0xx0']}
                ]


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
# print(board.get_possibilities(3, 2)[1])
# print(board.get_check_line(board.get_possibilities(3, 2)[1]))
print(board.best_lines(3, 2, pre_patterns))


