
class Board:
    def __init__(self, side):
        self.side = side
        self.board = []

    def create_board(self):
        for i in range(self.side):
            self.board.append([])

        for y in self.board:
            for x in range(self.side):
                y.append('')
        return self.board

    def last_step_check(self, char, pos):
        y = pos[0]
        x = pos[1]

        if self.check_horizontally(char, y, x):
            return self.check_horizontally(char, y, x)
        elif self.check_vertically(char, y, x):
            return self.check_vertically(char, y, x)
        elif self.check_diagonally1(char, y, x):
            return self.check_diagonally1(char, y, x)
        elif self.check_diagonally2(char, y, x):
            return self.check_diagonally2(char, y, x)
        else:
            return False

    def check_horizontally(self, char, y, x):
        pos_list = [[y, x]]
        start_x = x

        # go left
        while x > 0 and self.board[y][x-1] == char:
            previous_step_pos = [y, x-1]
            pos_list.insert(0, previous_step_pos)
            x -= 1
        # go right
        x = start_x
        while x < len(self.board)-1 and self.board[y][x+1] == char:
            previous_step_pos = [y, x+1]
            pos_list.append(previous_step_pos)
            x += 1

        if self.check_win(pos_list):
            return pos_list

    def check_vertically(self, num, y, x):
        pos_list = [[y, x]]
        start_y = y

        # go up
        while y > 0 and self.board[y-1][x] == num:
            previous_step_pos = [y-1, x]
            pos_list.insert(0, previous_step_pos)
            y -= 1
        # go down
        y = start_y
        while y < len(self.board)-1 and self.board[y+1][x] == num:
            previous_step_pos = [y+1, x]
            pos_list.append(previous_step_pos)
            y += 1

        if self.check_win(pos_list):
            return pos_list

    def check_diagonally1(self, num, y, x):
        pos_list = [[y, x]]
        start_y = y
        start_x = x

        # go left and up
        while y > 0 and x > 0 and self.board[y-1][x-1] == num:
            previous_step_pos = [y-1, x-1]
            pos_list.insert(0, previous_step_pos)
            y -= 1
            x -= 1
        # go right and down
        y = start_y
        x = start_x
        while y < len(self.board)-1 and x < len(self.board)-1 and self.board[y+1][x+1] == num:
            previous_step_pos = [y+1, x+1]
            pos_list.append(previous_step_pos)
            y += 1
            x += 1

        if self.check_win(pos_list):
            return pos_list

    def check_diagonally2(self, num, y, x):
        pos_list = [[y, x]]
        start_y = y
        start_x = x

        # go right and up
        while y > 0 and x < len(self.board)-1 and self.board[y-1][x+1] == num:
            previous_step_pos = [y-1, x+1]
            pos_list.insert(0, previous_step_pos)
            y -= 1
            x += 1
        # go left and down
        y = start_y
        x = start_x
        while y < len(self.board)-1 and x > 0 and self.board[y+1][x-1] == num:
            previous_step_pos = [y+1, x-1]
            pos_list.append(previous_step_pos)
            y += 1
            x -= 1

        if self.check_win(pos_list):
            return pos_list

    def check_win(self, pos_list):
        if len(pos_list) >= 5:
            print(pos_list)
            return True


# if __name__ == '__main__':
#     board = Board(10).create_board()
#     for row in board:
#         print(row)



