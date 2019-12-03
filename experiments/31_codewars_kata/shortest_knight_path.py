

import unittest
import queue


def knight(p1, p2):
    board_width = list('abcdefgh')
    x1 = board_width.index(list(p2)[0])+1
    y1 = int(list(p2)[1])
    # print('Target position is {} == [{}, {}]'.format(p2, x1, y1))

    x = board_width.index(list(p1)[0])+1
    y = int(list(p1)[1])
    # all possible movements for the knight
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    visited = []

    # create a queue and put first position (x, y) and 0 steps
    q = queue.Queue()
    q.put([x, y, 0])

    # while queue not empty
    while not q.empty():
        current = q.get()
        # print('Current position is {}, {}. Steps {}.'.format(current[0], current[1], current[2]))
        visited.append([current[0], current[1]])
        # print('Visited positions {}'.format(visited))
        for i in range(8):
            move_x = current[0]+dx[i]
            move_y = current[1]+dy[i]
            if move_x == x1 and move_y == y1:
                # print('Target is reached.')
                steps = current[2] + 1
                # print('Shortest path takes {} steps.'.format(steps))
                return steps
            if move_x in range(1, 9) and move_y in range(1, 9) and [move_x, move_y] not in visited:
                # print('From [{},{}] to [{},{}] {} steps. Target [{},{}] is not reached.'.format(x, y, move_x, move_y, current[2]+1, x1, y1))
                # add to queue possible movement
                q.put([move_x, move_y, current[2]+1])


class TestKnight(unittest.TestCase):
    arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]

    def test_knight(self):
        for x in self.arr:
            z = knight(x[0], x[1])
            self.assertTrue(z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z))


if __name__ == '__main__':
    unittest.main()
