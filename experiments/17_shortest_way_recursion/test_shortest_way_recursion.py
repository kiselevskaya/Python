
import unittest
from shortest_way_recursion import create_map, find_start, check_exit, find_exit


class CreateMapTestCase(unittest.TestCase):
    # Tests for 'create_map'
    def test_maze_exist(self):
        context = ['WWWWWWW\n', 'W     W\n', 'W W W W\n']
        self.assertIsNotNone(create_map(context))

    def test_is_list(self):
        context = ['WWWWWWW\n', 'W     W\n', 'W W W W\n']
        self.assertIsInstance(create_map(context), list)

    def test_right_maze(self):
        context = ['WWWWWWW\n', 'W     W\n', 'W W W W\n', 'W W W W\n', 'WSW W W\n', 'W W W W\n', 'WWWWW W\n']
        maze = create_map(context)
        for i in range(len(maze)):
            self.assertEqual(len(maze[0]), len(maze[i]))


class FindStartTestCase(unittest.TestCase):
    # Tests for 'find_start'

    def test_start_exist(self):
        context = ['WWWWWWW\n', 'W S   W\n', 'W W W W\n']
        self.assertTrue(find_start(context))


    def test_start_absent(self):
        context = ['WWWWWWW\n', 'W     W\n', 'W W W W\n']
        self.assertFalse(find_start(context))


class CheckExitTestCase(unittest.TestCase):
    # Tests for 'check_exit'

    def test_three_value_exit_exist(self):
        context = ['WWWWWWW\n', 'W     W\n', 'W W W W\n', 'W W W W\n', 'WSW W W\n', 'W W W W\n', 'WWWWW W\n']
        self.assertEqual(len(check_exit(context)), 3)

    def test_exit_exist(self):
        context = ['WWWWWWW\n', 'W     W\n', 'W W W W\n', 'W W W W\n', 'WSW W W\n', 'W W W W\n', 'WWWWWEW\n']
        self.assertTrue(check_exit(context)[0])

    @unittest.skip('"test_exit_absent" excess')
    def test_exit_absent(self):
        context = ['WWWWWWW\n', 'W     W\n', 'W W W W\n', 'W W W W\n', 'WSW W W\n', 'W W W W\n', 'WWWWWWW\n']
        self.assertFalse(check_exit(context)[0])

class FindExitTestCase(unittest.TestCase):
    # Tests for 'find_exit'

    def test_exit_absent(self):
        path = {}
        context = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', ' ', ' ', ' ', ' ', ' ', 'W'], ['W', ' ', 'W', ' ', 'W', ' ', 'W'], ['W', ' ', 'W', ' ', 'W', ' ', 'W'], ['W', 'S', 'W', ' ', 'W', ' ', 'W'], ['W', ' ', 'W', ' ', 'W', ' ', 'W'], ['W', 'W', 'W', 'W', 'W', ' ', 'W']]
        self.assertIsNone(find_exit(4, 1, context, path))

if __name__ == '__main__':
    unittest.main()
