# draw_horizontal_line.py


"""
Implement a function drawHorizontalLine(byte[] screen, int width, int x1, int x2, int y) which draws a horizontal line from (x1, y) to (x2, y).
"""


# def draw_horizontal_line(screen, width, x1, x2, y):
#     start = width*y
#     line = screen[start:start+width]
#     return ''.join(line)[x1:x2]


def draw_line(screen, width, x1, x2, y):
    result = bytearray([])
    start = x1 % 8
    start_byte = x1 // 8
    if start != 0:
        start_byte += 1

    end = x2 % 8
    end_byte = x2 // 8
    if end != 7:
        end_byte -= 1

    # full bytes
    mask = int('1'*8, 2)
    for b in range(start_byte, end_byte+1):
        result.append(screen[width//8*y + b] & mask)

    # create masks for start and end
    start_mask = int('1'*(8-start), 2)
    end_mask = int('1'*(end+1), 2) << (7-end)

    if x1 // 8 == x2 // 8:
        mask = start_mask & end_mask
        result.append(screen[width//8*y + x1//8] & mask)
    else:
        if start != 0:
            result.insert(0, screen[width//8*y + start_byte-1] & start_mask)
        if end != 7:
            result.append(screen[width//8*y + end_byte+1] & end_mask)
    return result


if __name__ == '__main__':
    # a = [int(bin(i)[2:]) for i in range(128, 152)]
    # assert draw_horizontal_line(array, 8, 31, 53, 2) == '1100101001001010110010', 'Test Failed'

    array = bytearray([int(bin(i), 2) for i in range(128, 152)])
    assert [bin(i) for i in draw_line(array, 48, 8, 14, 1)] == ['0b10000110'], 'Test 1 failed'
    assert [bin(i) for i in draw_line(array, 48, 1, 20, 1)] == ['0b110', '0b10000111', '0b10001000'], 'Test 2 failed'
    assert [bin(i) for i in draw_line(array, 48, 0, 8, 1)] == ['0b10000110', '0b10000000'], 'Test 3 failed'
    assert [bin(i) for i in draw_line(array, 48, 0, 15, 1)] == ['0b10000110', '0b10000111'], 'Test 4 failed'
