

from queue import Queue
import re


def break_pieces(shape):
    pieces = []  # List of pieces onto which breaks the given shape
    list_shape = [list(x) for x in shape.splitlines()]  # Represents the shape as list of consequent strings
    q = Queue()  # Initiates the Queue
    height = len(list_shape)
    width = max([len(x) for x in list_shape])

    # Finds all corners of the shape and puts into queue their coordinates ([y, x])
    for i in range(height):
        for j in range(width):
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
                continue
        except IndexError:
            pass

        piece = [[' ']*width for _ in range(height)]  # Empty nested list of size list_shape, initiated for each piece
        while not queue.empty():
            [y, x] = queue.get()  # Takes next coordinate of the same piece from the queue
            try:  # Step right check
                if list_shape[y][x+1] == ' ':
                    if x+1 == width-1:  # Breaks the loop if realise it walks in the gap of shape
                        piece = False
                        break
                    queue.put([y, x+1])  # Adds next position of the same piece to the queue
                    list_shape[y][x+1] = '0'  # Marks with '0' visited coordinate
                elif list_shape[y][x+1] == '|':  # Draw wall on the right side
                    piece[y][x+1] = '|'
                    if list_shape[y-1][x] == '-':  # Draws up right corner
                        piece[y-1][x+1] = '+'
                    if list_shape[y+1][x] == '-':  # Draws down right corner
                        piece[y+1][x+1] = '+'
                elif list_shape[y][x+1] == '+':  # Gets rid of unnecessary '+' on the right wall
                    if list_shape[y-1][x+1] == '|' and list_shape[y+1][x+1] == '|':
                        piece[y][x+1] = '|'
                    else:
                        piece[y][x+1] = '+'
            except IndexError:
                pass

            try:  # Step down check
                if list_shape[y+1][x] == ' ':
                    if y+1 == height-1:  # Breaks the loop if realise it walks in the gap of shape
                        piece = False
                        break
                    queue.put([y+1, x])  # Adds next position of the same piece to the queue
                    list_shape[y+1][x] = '0'  # Marks with '0' visited coordinate
                elif list_shape[y+1][x] == '-':  # Draw the down wall
                    piece[y+1][x] = '-'
                elif list_shape[y+1][x] == '+':  # Gets rid of unnecessary '+' on the down wall
                    if list_shape[y+1][x-1] == '-' and list_shape[y+1][x+1] == '-':
                        piece[y+1][x] = '-'
                    else:
                        piece[y+1][x] = '+'
            except IndexError:
                pass

            try:  # Step left check
                if list_shape[y][x-1] == ' ':  # Breaks the loop if realise it walks in the gap of shape
                    if x-1 == 0:
                        piece = False
                        break
                    queue.put([y, x-1])  # Adds next position of the same piece to the queue
                    list_shape[y][x-1] = '0'  # Marks with '0' visited coordinate
                elif list_shape[y][x-1] == '|':  # Draw the left wall
                    piece[y][x-1] = '|'
                    if list_shape[y-1][x] == '-':  # Draws up left corner
                        piece[y-1][x-1] = '+'
                    if list_shape[y+1][x] == '-':  # Draws down left corner
                        piece[y+1][x-1] = '+'
                elif list_shape[y][x-1] == '+':  # Gets rid of unnecessary '+' on the left wall
                    if list_shape[y-1][x-1] == '|' and list_shape[y+1][x-1] == '|':
                        piece[y][x-1] = '|'
                    else:
                        piece[y][x-1] = '+'
            except IndexError:
                pass

            try:  # Step up check
                if list_shape[y-1][x] == ' ':  # Breaks the loop if realise it walks in the gap of shape
                    if y-1 == 0:
                        piece = False
                        break
                    queue.put([y-1, x])  # Adds next position of the same piece to the queue
                    list_shape[y-1][x] = '0'  # Marks with '0' visited coordinate
                elif list_shape[y-1][x] == '-':  # Draw the up wall
                    piece[y-1][x] = '-'
                elif list_shape[y-1][x] == '+':  # Gets rid of unnecessary '+' on the up wall
                    if list_shape[y-1][x-1] == '-' and list_shape[y-1][x+1] == '-':
                        piece[y-1][x] = '-'
                    else:
                        piece[y-1][x] = '+'
            except IndexError:
                pass

        try:
            piece = [''.join(x) for x in piece if any(z in ['+', '-', '|'] for z in x)]  # Join lists into strings and cut if empty
        except TypeError:
            pass

        if piece:
            start = min([re.search('[+-|]', x).start() for x in piece])  # Cuts spaces before piece
            piece = '\n'.join([x[start:].rstrip() for x in piece])
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

shape2 = '\n'.join(['         +-+        ',
                    '         | |        ',
                    '       +-+-+-+      ',
                    '       |     |      ',
                    '    +--+-----+--+   ',
                    '    |           |   ',
                    ' +--+-----------+--+',
                    ' |                 |',
                    ' +-----------------+'])

shape3 = '\n'.join(['+-------------------+--+',
                    '|                   |  |',
                    '|                   |  |',
                    '|  +----------------+  |',
                    '|  |                   |',
                    '|  |                   |',
                    '+--+-------------------+'])

for i in break_pieces(shape3):
    print(i)
