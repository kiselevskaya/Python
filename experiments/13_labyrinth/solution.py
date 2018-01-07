# -*- coding: utf-8 -*-

import queue

def create_maze(rows):
    result = []
    for row in rows:
        row = row[0:-1]
        subarr = []
        for char in row:
            subarr.append(char)
        result.append(subarr)
    return result

def print_map(maze):
    for arr in maze:
        print (arr)

def find_start(rows):
    for y in range(len(rows)):
        row = rows[y]
        for x in range(len(row)):
            if row[x] == 'S':
                return (y, x)

def make_step(y, x, q, maze):
    if maze[y][x] == ' ':
        maze[y][x] = '0'
        q.put([y, x])

def find_exit(maze, q):
    height = len(maze)
    width = len(maze[0])
    while not q.empty():
        step = q.get()
        #up
        if step[0] > 0:
            make_step(step[0]-1, step[1], q, maze)
        #down
        if step[0] < height-1:
            make_step(step[0]+1, step[1], q, maze)
        #left
        if step[1] > 0:
            make_step(step[0], step[1]-1, q, maze)
        #right
        if step[1] < width-1:
            make_step(step[0], step[1]+1, q, maze)

def check_exit(maze):
    for x in maze[0]:
        if x != 'W' and x == '0':
            return True
    for x in maze[-1]:
        if x != 'W' and x == '0':
            return True
    for i in maze:
        if i[0] != 'W' and i[0] == '0':
            return True
    for i in maze:
        if i[-1] != 'W' and i[-1] == '0':
            return True
    return False

if __name__ == '__main__':
    file = open('../00_text_files/09_labyrinth.txt', 'rt')
    rows = file.readlines()
    file.close()
    maze = create_maze(rows)
    start = find_start(rows)
    maze[start[0]][start[1]] = '0'
    q = queue.Queue()
    q.put(start)
    find_exit(maze, q)
    print(check_exit(maze))
    print_map(maze)
