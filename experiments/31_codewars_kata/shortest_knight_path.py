

# import unittest
# import queue


def knight(p1, p2):
    board_width = list('abcdefgh')
    x1 = board_width.index(list(p2)[0])+1
    y1 = int(list(p2)[1])
    x = board_width.index(list(p1)[0])+1
    y = int(list(p1)[1])
    # all possible movements for the knight
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    visited = []
    steps = 0
    # create a queue and put first position, 0 steps
    # make a function to recurse
    # while queue not empty
    # take first element from the queue
    # add current position to visited list
    # find possible movements and compare with target position
    # if target not reached, increase steps by 1 and add moves to queue
    visited.append([x, y])
    for i in range(8):
        move_x = x+dx[i]
        move_y = y+dy[i]
        if move_x == x1 and move_y == y1:
            # stop queue
            return steps+1
        if move_x in range(9) and move_y in range(9) and [move_x, move_y] not in visited:
            print('From [{},{}] to [{},{}] {} steps. Target is [{},{}] Visited cells {}'.format(x, y, move_x, move_y, steps+1, x1, y1, visited))
            # add to queue possible movement


knight('a1', 'c1')


# class TestKnight(unittest.TestCase):
#     arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
#
#     def test_knight(self):
#         for x in self.arr:
#             # self.assertEqual(knight(x[0], x[1]), x[2])
#             z = knight(x[0], x[1])
#             # self.expect(z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z))
#             self.assert_(z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z))


# if __name__ == '__main__':
#     unittest.main()
