# -*- coding: utf-8 -*-

def create_map(rows):
    maze = []
    for row in rows:
        row = row[:-1]
        subarr = []
        for i in row:
            subarr.append(i)
        maze.append(subarr)
    return maze

def print_map(chart):
    for subarr in chart:
        print (subarr)

def find_start(chart):
    for y in range(len(chart)):
        row = chart[y]
        for x in range(len(row)):
            if row[x] == 'S':
                return (y, x)

def make_step(y, x, chart):
    if chart[y][x] == ' ':
        chart[y][x] = '0'

def find_exit(y, x, chart):
    h = len(chart)
    w = len(chart[0])
    #left
    if x-1 == 0 and chart[y][x-1] == ' ':
        chart[y][x-1] = 'E'
        return chart[y][x-1]
    elif x-1 > 0 and chart[y][x-1] == ' ':
        chart[y][x-1] = '0'
        find_exit(y, x-1, chart)
    #up
    if y-1 == 0 and chart[y-1][x] == ' ':
        chart[y-1][x] = 'E'
        return chart[y-1][x]
    elif y-1 > 0 and chart[y-1][x] == ' ':
        chart[y-1][x] = '0'
        find_exit(y-1, x, chart)
    #right
    if x+1 == w-1 and chart[y][x+1] == ' ':
        chart[y][x+1] = 'E'
        return chart[y][x+1]
    elif x+1 < w - 1 and chart[y][x+1] == ' ':
        chart[y][x+1] = '0'
        find_exit(y, x+1, chart)
    #down
    if y+1 == h-1 and chart[y+1][x] == ' ':
        chart[y+1][x] = 'E'
        return chart[y+1][x]
    elif y+1 < h - 1 and chart[y+1][x] == ' ':
        chart[y+1][x] = '0'
        find_exit(y+1, x, chart)

def check_exit(chart):
    for u in chart[0]:
        if u == 'E':
            return True
    for d in chart[-1]:
        if d == 'E':
            return True
    for l in chart:
        if l[0] == 'E':
            return True
    for r in chart:
        if r[-1] == 'E':
            return True
    return False

if __name__ == '__main__':
    file = open('../00_text_files/01_labyrinth.txt', 'rt')
    labyrinth = file.readlines()
    file.close()
    maze = create_map(labyrinth)
    start = find_start(maze)
    maze[start[0]][start[1]] = '0'
    find_exit(start[0], start[1], maze)
    print_map(maze)
    print (check_exit(maze))
