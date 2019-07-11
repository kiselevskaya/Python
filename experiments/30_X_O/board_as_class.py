

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
        self.get_possibilities(ch, y, x)
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
            self.potential_steps += (list(line[i][1] for i in range(len(line)) if line[i][0] == '' and line[i][1] not in self.potential_steps))
        try:
            self.potential_steps.pop(self.potential_steps.index([y, x]))
        except ValueError:
            print('Not in list')
        return self.potential_steps

    def get_value(self):
        # values = [[{'value': 5, 'pos': [1, 2]},...{...}],[{'value': 10, 'pos': [3, 4]},...{...}]] first list for 'X' second - for 'O'
        values = [[], []]
        # check by example just on first possible step in all which are in potential steps list
        print('Potential steps: ', self.potential_steps)
        for j in range(len(self.potential_steps)):
            y = self.potential_steps[j][0]
            x = self.potential_steps[j][1]
            for line in self.directions(y, x):
                indx = [i for i in range(len(line)) if line[i][1] == [y, x]][0]
                line[indx][0] = '7'
                txt = ''.join(map(lambda x: '0' if x == '' else x, list(line[i][0] for i in range(len(line)))))
                txt = re.sub('[x]', '1', txt)
                txt = re.sub('[o]', '2', txt)
                for k in range(len(compare_with[1])):
                    if re.match(compare_with[1][k], txt):
                        values[0].append([compare_with[0][k], [y, x]])
                    if re.match(compare_with[2][k], txt):
                        values[1].append([compare_with[0][k], [y, x]])
        return values


board = Board()
import random

class Computer:
    def __init__(self, ch='x'):
        self.attack = None
        self.defense = None
        self.y = board.center
        self.x = board.center
        self.ch = ch
        self.radius = board.radius

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def make_step(self, y=None, x=None, ch=None):
        if ch or y or x is not None: self.ch, self.y, self.x = ch, y, x
        board.make_step(self.ch, self.y, self.x)

    def get_next_step(self):
        if self.ch == 'x':
            self.attack = self.best_option(board.get_value()[0])
            self.defense = self.best_option(board.get_value()[1])
        else:
            self.attack = self.best_option(board.get_value()[1])
            self.defense = self.best_option(board.get_value()[0])
        print('Best po for attack: ', self.attack)
        print('Best pos for defence: ', self.defense)
        for pos in self.attack[0]:
            if pos in self.defense[0]:
                return pos
            elif self.attack[0][1] < self.defense[0][1]:
                return random.choice(self.defense[0])
            else:
                return random.choice(self.attack[0])

    def best_option(self, val_pos):
        max_value = max(list(i[0] for i in val_pos))
        print('Max value: ', max_value)
        max_val_pos = list(e[1] for e in val_pos if e[0] == max_value)
        print('Positions for max value: ', max_val_pos)

        occurrences = lambda s, lst: (i for i, e in enumerate(lst) if e == s)

        repeat = list(list(occurrences(i, max_val_pos)) for i in max_val_pos)
        print('Current index pos repeats in indexes: ', repeat)
        frequency = max(list(len(list(occurrences(i, max_val_pos))) for i in max_val_pos))
        print('Max frequency for positions with max value', frequency)

        #   list of indexes with more frequent position
        best_pos_index = list(set(sum(list(j for j in repeat if len(j) == frequency), [])))
        print('List of indexes with more frequent position: ', best_pos_index)

        best_pos = list()
        for pos in list(max_val_pos[i] for i in best_pos_index):
            if pos not in best_pos:
                best_pos.append(pos)
        print('List of pos for best next step: ', best_pos)
        return [best_pos, max_value]


field = board.create_board()

ai = Computer()
ai.make_step()
print(board.get_field())
print()

board.make_step('x', 1, 2)
board.make_step('o', 2, 1)
print(board.get_field())
board.get_possibilities('o', 2, 1)
print()
print(ai.get_next_step())
