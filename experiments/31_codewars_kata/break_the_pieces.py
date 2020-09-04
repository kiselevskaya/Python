

from queue import Queue
import re


def break_pieces(shape):
    pieces = []  # List of pieces onto which breaks the given shape
    list_shape = [list(x) for x in shape.splitlines()]  # Represents the shape as list of consequent strings
    q = Queue()  # Initiates the Queue

    # Finds all corners of the shape and puts into queue their coordinates ([y, x])
    for i in range(len(list_shape)):
        for j in range(len(list_shape[0])):
            if list_shape[i][j] == '+':
                q.put([i, j])

    # Runs through all corners ('+') to not miss any piece
    while not q.empty():
        [y, x] = q.get()  # Gets coordinates ([y, x]) of the next corner
        queue = Queue()  # Initiates the Queue to go through (search in breadth) inner space in the piece
        try:
            if list_shape[y+1][x+1] == ' ':
                queue.put([y+1, x+1])
                list_shape[y+1][x+1] = '0'
            else:
                break
        except IndexError:
            pass

        piece = [[' ']*len(list_shape[0]) for _ in range(len(list_shape))]  # Empty nested list of size list_shape
        while not queue.empty():
            [y, x] = queue.get()
            try:  # Step right
                if list_shape[y][x+1] == ' ':
                    if x+1 == len(list_shape[0])-1:
                        piece = False
                        break
                    queue.put([y, x+1])
                    list_shape[y][x+1] = '0'
                elif list_shape[y][x+1] in ['|', '+']:  # Gets rid of unnecessary '+' on side of piece
                    piece[y][x+1] = '|'
                    if list_shape[y-1][x] == '-':  # Draws up right corner
                        piece[y-1][x+1] = '+'
                    elif list_shape[y+1][x] == '-':  # Draws down right corner
                        piece[y+1][x+1] = '+'
            except IndexError:
                pass
            try:  # Step down
                if list_shape[y+1][x] == ' ':
                    if y+1 == len(list_shape)-1:
                        piece = False
                        break
                    queue.put([y+1, x])
                    list_shape[y+1][x] = '0'
                elif list_shape[y+1][x] in ['-', '+']:  # Gets rid of unnecessary '+' on side of piece
                    piece[y+1][x] = '-'
            except IndexError:
                pass
            try:  # Step left
                if list_shape[y][x-1] == ' ':
                    if x-1 == 0:
                        piece = False
                        break
                    queue.put([y, x-1])
                    list_shape[y][x-1] = '0'
                elif list_shape[y][x-1] in ['|', '+']:
                    piece[y][x-1] = '|'
                    if list_shape[y-1][x] == '-':  # Draws up left corner
                        piece[y-1][x-1] = '+'
                    elif list_shape[y+1][x] == '-':  # Draws down right corner
                        piece[y+1][x-1] = '+'
            except IndexError:
                pass
            try:  # Step up
                if list_shape[y-1][x] == ' ':
                    if y-1 == 0:
                        piece = False
                        break
                    queue.put([y-1, x])
                    list_shape[y-1][x] = '0'
                elif y-1 >= 0 and list_shape[y-1][x] in ['-', '+']:  # Gets rid of unnecessary '+' on side of piece
                    piece[y-1][x] = '-'
            except IndexError:
                pass

        piece = [''.join(x) for x in piece if any(z in ['+', '-', '|'] for z in x)]  # Join lists into strings and cut if empty
        if piece:
            start = min([re.search('[+-|]', x).start() for x in piece])  # Cuts spaces before piece
            end = max([max([i for i, item in enumerate(x) if re.match('[+-|]', item)]) for x in piece])  # Cuts spaces after piece
            piece = '\n'.join([x[start:end+1] for x in piece])
            pieces.append(piece)

    return pieces


shape = '\n'.join(["+------------+",
                   "|            |",
                   "|            |",
                   "|            |",
                   "+------+-----+",
                   "|      |     |",
                   "|      |     |",
                   "+------+-----+"])

solution = ['\n'.join(["+------------+",
                       "|            |",
                       "|            |",
                       "|            |",
                       "+------------+"]),
            '\n'.join(["+------+",
                       "|      |",
                       "|      |",
                       "+------+"]),
            '\n'.join(["+-----+",
                       "|     |",
                       "|     |",
                       "+-----+"])]

assert sorted(break_pieces(shape)) == sorted(solution)
