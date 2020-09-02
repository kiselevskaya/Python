

from queue import Queue


def break_pieces(shape):
    pieces = []  # List of pieces onto which breaks the given shape
    list_shape = shape.splitlines()  # Represents the shape as list of consequent strings
    q = Queue()  # Initiates the Queue
    # Puts into queue coordinates ([y, x]) of the upper left corner of the first piece in the shape
    q.put([0, list_shape[0].find('+')])
    # while not q.empty():  # Goes through the shape while not all pieces are found
    piece = [' '.join(['']*len(list_shape[0])) for _ in range(len(list_shape))]  # List of empty string
    [y, x] = q.get()  # Gets coordinates ([y, x]) of the corner of the next piece
    queue = Queue()
    if list_shape[y+1][x+1] == ' ':
        queue.put([y+1, x+1])
        list_shape[y+1][x+1] = '0'
    print(piece)
    return pieces


shape = '\n'.join(["+------------+",
                   "|            |",
                   "|            |",
                   "|            |",
                   "+------+-----+",
                   "|      |     |",
                   "|      |     |",
                   "+------+-----+"])

print(break_pieces(shape))


# solution = ['\n'.join(["+------------+",
#                        "|            |",
#                        "|            |",
#                        "|            |",
#                       "+------------+"]),
#             '\n'.join(["+------+",
#                        "|      |",
#                        "|      |",
#                        "+------+"]),
#             '\n'.join(["+-----+",
#                        "|     |",
#                        "|     |",
#                        "+-----+"])]
#
# test.assert_equals(sorted(break_pieces(shape)), sorted(solution))
