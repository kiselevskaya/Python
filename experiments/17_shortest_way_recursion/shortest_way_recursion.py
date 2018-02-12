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
        print(subarr)


def find_start(chart):
    for y in range(len(chart)):
        row = chart[y]
        for x in range(len(row)):
            if row[x] == 'S':
                return (y, x)


def find_exit(y, x, chart, path):
    h = len(chart)
    w = len(chart[0])
    # left
    if x-1 == 0 and chart[y][x-1] == ' ':
        chart[y][x-1] = 'E'
        path[(y, x-1)] = [y, x]
        return
    elif x-1 > 0 and chart[y][x-1] == ' ':
        chart[y][x-1] = '0'
        path[(y, x - 1)] = [y, x]
        find_exit(y, x-1, chart, path)
    # up
    if y-1 == 0 and chart[y-1][x] == ' ':
        chart[y-1][x] = 'E'
        path[(y-1, x)] = [y, x]
        return
    elif y-1 > 0 and chart[y-1][x] == ' ':
        chart[y-1][x] = '0'
        path[(y - 1, x)] = [y, x]
        find_exit(y-1, x, chart, path)
    # right
    if x+1 == w-1 and chart[y][x+1] == ' ':
        chart[y][x+1] = 'E'
        path[(y, x+1)] = [y, x]
        return
    elif x+1 < w - 1 and chart[y][x+1] == ' ':
        chart[y][x+1] = '0'
        path[(y, x + 1)] = [y, x]
        find_exit(y, x+1, chart, path)
    # down
    if y+1 == h-1 and chart[y+1][x] == ' ':
        chart[y+1][x] = 'E'
        path[(y+1, x)] = [y, x]
        return
    elif y+1 < h - 1 and chart[y+1][x] == ' ':
        chart[y+1][x] = '0'
        path[(y + 1, x)] = [y, x]
        find_exit(y+1, x, chart, path)


def check_exit(chart):
    height = len(chart)
    width = len(chart[0])

    for x in range(width):
        v = chart[0][x]
        if v == 'E':
            return True, 0, x
        v = chart[height-1][x]
        if v == 'E':
            return True, height-1, x

    for y in range(height):
        v = chart[y][0]
        if v == 'E':
            return True, y, 0
        v = chart[y][width-1]
        if v == 'E':
            return True, y, width-1

    return False, -1, -1


if __name__ == '__main__':
    file = open('../00_text_files/01_labyrinth.txt', 'rt')
    labyrinth = file.readlines()
    file.close()
    maze = create_map(labyrinth)
    start = find_start(maze)
    maze[start[0]][start[1]] = '0'
    path = {}
    find_exit(start[0], start[1], maze, path)
    print_map(maze)

    ex = check_exit(maze)
    if ex[0]:
        y = ex[1]
        x = ex[2]
        print([y, x, maze[y][x]])
        while True:
            coord = (y, x)
            if coord in path:
                y, x = path[coord]
                print([y, x, maze[y][x]])
            else:
                break
    else:
        print("NO WAY")
