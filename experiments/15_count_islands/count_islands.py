# -*- coding: utf-8 -*-


def create_map(rows):
    arr = []
    for row in rows:
        row = row[:-1]
        sa = []
        for r in row:
            sa.append(r)
        arr.append(sa)
    return arr


def print_map(arr):
    for i in arr:
        print(i)


def check_connections(y, x, arr):
    height = len(arr)
    width = len(arr[0])
    # NorthWest
    if y-1 >= 0 and x-1 >= 0 and arr[y-1][x-1] == '.':
        arr[y-1][x-1] = '^'
        check_connections(y - 1, x - 1, arr)
    # North
    if y-1 >= 0 and arr[y-1][x] == '.':
        arr[y-1][x] = '^'
        check_connections(y - 1, x, arr)
    # NorthEast
    if y-1 >= 0 and x+1 <= width-1 and arr[y-1][x+1] == '.':
        arr[y-1][x+1] = '^'
        check_connections(y - 1, x + 1, arr)
    # East
    if x+1 <= width-1 and arr[y][x+1] == '.':
        arr[y][x+1] = '^'
        check_connections(y, x + 1, arr)
    # SouthEast
    if y+1 <= height-1 and x+1 <= width-1 and arr[y+1][x+1] == '.':
        arr[y+1][x+1] = '^'
        check_connections(y + 1, x + 1, arr)
    # South
    if y+1 <= height-1 and arr[y+1][x] == '.':
        arr[y+1][x] = '^'
        check_connections(y + 1, x, arr)
    # SouthWest
    if y+1 <= height-1 and x-1 >= 0 and arr[y+1][x-1] == '.':
        arr[y+1][x-1] = '^'
        check_connections(y + 1, x - 1, arr)
    # West
    if x-1 >= 0 and arr[y][x-1] == '.':
        arr[y][x-1] = '^'
        check_connections(y, x - 1, arr)


def get_islands_amount(arr):
    count = 0
    for i in range(len(arr)):
        subarr = arr[i]
        for j in range(len(subarr)):
            if subarr[j] == '.':
                subarr[j] = '^'
                check_connections(i, j, arr)
                count += 1
    return count


if __name__ == '__main__':
    file = open('../00_text_files/01_islands.txt', 'rt')
    content = file.readlines()
    file.close()
    sea = create_map(content)
    print (get_islands_amount(sea))
    print_map(sea)
