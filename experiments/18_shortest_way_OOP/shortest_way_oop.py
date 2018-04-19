# -*- coding: utf-8 -*-


class Maze:
    def __init__(self, maze_map):
        self.maze_map = [list(arr[0]) for arr in [l.split('\n') for l in open(maze_map, 'rt')]]
        self.start = self.find_start()
        self.path = {}
        self.maze_map[self.start.y][self.start.x] = '0'
        self.h = len(self.maze_map)
        self.w = len(self.maze_map[0])

    def find_start(self):
        for y in range(len(self.maze_map)):
            row = self.maze_map[y]
            for x in range(len(row)):
                if row[x] == 'S':
                    return Coord(y, x)

    def print_map(self):
        for arr in self.maze_map:
            print(arr)

    def find_exit(self, c=None):
        if c is None:
            c = self.start

        if c.y == 0 or c.y == self.h-1 or c.x == 0 or c.x == self.w-1:
            self.maze_map[c.y][c.x] = 'E'
            return

        left = c.left_step()
        if left.x >= 0 and left.check_maze_empty(self.maze_map):
            self.make_step(c, left)

        up = c.up_step()
        if up.y >= 0 and up.check_maze_empty(self.maze_map):
            self.make_step(c, up)

        right = c.right_step()
        if right.x <= self.w - 1 and right.check_maze_empty(self.maze_map):
            self.make_step(c, right)

        down = c.down_step()
        if down.y <= self.h - 1 and down.check_maze_empty(self.maze_map):
            self.make_step(c, down)

    def make_step(self, c_from, c_to):
        c_to.set_maze_zero(self.maze_map)
        self.path[c_to] = c_from
        self.find_exit(c_to)

    def check_exit(self):
        for x in range(self.w):
            v = self.maze_map[0][x]
            if v == 'E':
                return True, Coord(0, x)
            v = self.maze_map[self.h-1][x]
            if v == 'E':
                return True, Coord(self.h-1, x)
        for y in range(self.h):
            v = self.maze_map[y][0]
            if v == 'E':
                return True, Coord(y, 0)
            v = self.maze_map[y][self.w-1]
            if v == 'E':
                return True, Coord(y, self.w-1)
        return False, Coord(-1, -1)

    def get_path(self):
        ext = self.check_exit()
        if ext[0]:
            c = ext[1]
            print([c.y, c.x, self.maze_map[c.y][c.x]])
            while True:
                if c in self.path:
                    c = self.path[c]
                    print([c.y, c.x, self.maze_map[c.y][c.x]])
                else:
                    break
        else:
            print("NO WAY")


class Coord:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '({}, {})'.format(self.y, self.x)

    def left_step(self):
        return Coord(self.y, self.x-1)

    def up_step(self):
        return Coord(self.y-1, self.x)

    def right_step(self):
        return Coord(self.y, self.x+1)

    def down_step(self):
        return Coord(self.y+1, self.x)

    def check_maze_empty(self, maze):
        return maze[self.y][self.x] == ' '

    def set_maze_zero(self, maze):
        maze[self.y][self.x] = '0'


if __name__ == '__main__':
    maze = Maze('../00_text_files/01_labyrinth.txt')
    maze.find_exit()

    maze.print_map()
    print(maze.check_exit())
    maze.get_path()
