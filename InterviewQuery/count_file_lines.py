

def count_lines(filepath):
    file = open(filepath, 'r')

    count = 0
    buf_size = 1024*1024
    buf = file.read(buf_size)

    while buf:
        count += buf.count('\n')
        buf = file.read(buf_size)

    return count


# if __name__ == '__main__':
#     # Test 1
#     result = count_lines(input)
#     assert result == output, f'Test #1 Failed\nExpected: {output}\nResult: {result}\n'
