# -*- coding: utf-8 -*-

import queue
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def create_maze(rows):
    result = []
    for row in rows:
        row = row[:-1]
        sa = []
        for char in row:
            if char == 'W':
                char = -1
            elif char == ' ':
                char = random.randrange(10)
            elif char == 'S':
                char = 0
            sa.append(char)
        result.append(sa)
    return result


def create_time_maze(arr):
    new_arr = []
    for row in arr:
        sa = []
        for i in row:
            if isinstance(i, int) and i > -1:
                i = 1000
            sa.append(i)
        new_arr.append(sa)
    return new_arr


def print_map(arr):
    for sa in arr:
        print(sa)


def find_start(rows):
    for y in range(len(rows)):
        row = rows[y]
        for x in range(len(row)):
            if row[x] == 'S':
                return y, x


def make_step(y, x, q, arr, time_arr, step, path):
    u = step[0]
    v = step[1]
    if time_arr[y][x] > time_arr[u][v] + arr[y][x]:
        time_arr[y][x] = time_arr[u][v] + arr[y][x]
        q.put([y, x])
        path[(y, x)] = [u, v]


def find_exit(arr, q, time_arr):
    path = {}
    height = len(arr)
    width = len(arr[0])
    while not q.empty():
        step = q.get()
        #up
        if step[0] > 0:
            make_step(step[0] - 1, step[1], q, arr, time_arr, step, path)
        #down
        if step[0] < height-1:
            make_step(step[0] + 1, step[1], q, arr, time_arr, step, path)
        #left
        if step[1] > 0:
            make_step(step[0], step[1] - 1, q, arr, time_arr, step, path)
        #right
        if step[1] < width-1:
            make_step(step[0], step[1] + 1, q, arr, time_arr, step, path)
    return path


def check_exit(arr):
    height = len(arr)
    width = len(arr[0])

    for x in range(width):
        v = arr[0][x]
        if v != -1 and v != 1000:
            return True, 0, x
        v = arr[height-1][x]
        if v != -1 and v != 1000:
            return True, height-1, x

    for y in range(height):
        v = arr[y][0]
        if v != -1 and v != 1000:
            return True, y, 0
        v = arr[y][width-1]
        if v != -1 and v != 1000:
            return True, y, width-1

    return False, -1, -1


if __name__ == '__main__':
    file = open('../00_text_files/01_labyrinth.txt', 'rt')
    content = file.readlines()
    file.close()

    maze = create_maze(content)
    min_time = create_time_maze(maze)

    start = find_start(content)

    q = queue.Queue()

    maze[start[0]][start[1]] = 0
    min_time[start[0]][start[1]] = 0

    q.put(start)

    path = find_exit(maze, q, min_time)

    ex = check_exit(min_time)
    if ex[0]:
        y = ex[1]
        x = ex[2]
        print([y, x, min_time[y][x]])
        while True:
            coord = (y, x)
            if coord in path:
                y, x = path[coord]
                print([y, x, min_time[y][x]])
            else:
                break
    else:
        print("NO WAY")

    print_map(maze)
