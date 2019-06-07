

def create_board(side):
    board = []
    for i in range(side):
        board.append([])
    for y in board:
        for x in range(side):
            y.append('')
    return board


def board_step(board, char, pos):
    if board[pos[0]][pos[1]] == '':
        board[pos[0]][pos[1]] = char
    return board


def last_step_check(board, char, pos):
    y = pos[0]
    x = pos[1]

    if check_win(check_horizontally(board, char, y, x)):
        return check_horizontally(board, char, y, x)
    elif check_win(check_vertically(board, char, y, x)):
        return check_vertically(board, char, y, x)
    elif check_win(check_diagonally1(board, char, y, x)):
        return check_diagonally1(board, char, y, x)
    elif check_win(check_diagonally2(board, char, y, x)):
        return check_diagonally2(board, char, y, x)
    else:
        return False


def check_horizontally(board, char, y, x):
    pos_list = [[y, x]]
    start_x = x

    # go left
    while x > 0 and board[y][x-1] == char:
        previous_step_pos = [y, x-1]
        pos_list.insert(0, previous_step_pos)
        x -= 1
    # go right
    x = start_x
    while x < len(board)-1 and board[y][x+1] == char:
        previous_step_pos = [y, x+1]
        pos_list.append(previous_step_pos)
        x += 1
    return pos_list


def check_vertically(board, char, y, x):
    pos_list = [[y, x]]
    start_y = y

    # go up
    while y > 0 and board[y-1][x] == char:
        previous_step_pos = [y-1, x]
        pos_list.insert(0, previous_step_pos)
        y -= 1
    # go down
    y = start_y
    while y < len(board)-1 and board[y+1][x] == char:
        previous_step_pos = [y+1, x]
        pos_list.append(previous_step_pos)
        y += 1
    return pos_list


def check_diagonally1(board, char, y, x):
    pos_list = [[y, x]]
    start_y = y
    start_x = x

    # go left and up
    while y > 0 and x > 0 and board[y-1][x-1] == char:
        previous_step_pos = [y-1, x-1]
        pos_list.insert(0, previous_step_pos)
        y -= 1
        x -= 1
    # go right and down
    y = start_y
    x = start_x
    while y < len(board)-1 and x < len(board)-1 and board[y+1][x+1] == char:
        previous_step_pos = [y+1, x+1]
        pos_list.append(previous_step_pos)
        y += 1
        x += 1
    return pos_list


def check_diagonally2(board, char, y, x):
    pos_list = [[y, x]]
    start_y = y
    start_x = x

    # go right and up
    while y > 0 and x < len(board)-1 and board[y-1][x+1] == char:
        previous_step_pos = [y-1, x+1]
        pos_list.insert(0, previous_step_pos)
        y -= 1
        x += 1
    # go left and down
    y = start_y
    x = start_x
    while y < len(board)-1 and x > 0 and board[y+1][x-1] == char:
        previous_step_pos = [y+1, x-1]
        pos_list.append(previous_step_pos)
        y += 1
        x -= 1
    return pos_list


def check_win(pos_list):
    if len(pos_list) >= 5:
        return True
