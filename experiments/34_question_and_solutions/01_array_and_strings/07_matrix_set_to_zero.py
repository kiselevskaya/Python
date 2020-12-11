# 07_matrix_set_to_zero.py


'''Write an algorithm such that if an element in matrix MxN is 0, its entire row and column are set to 0'''


# Let assume that only zeros that were at the beginning have been taken into a count for further change
# def set_to_zero(matrix):
#     m, n = len(matrix), len(matrix[0])
#     # Row by row run through the matrix if 0 -> add coordinates into new created list
#     pos_zero = []
#     for y in range(m):
#         for x in range(n):
#             if matrix[y][x] == 0:
#                 pos_zero.append([y, x])
#     xs = [i[1] for i in pos_zero]
#     ys = [i[0] for i in pos_zero]
#     matrix = [list(map(lambda _: 0, matrix[i])) if i in ys else matrix[i] for i in range(m)]
#     matrix = [[0 if x in xs else matrix[y][x] for x in range(n)] for y in range(m)]
#     return matrix


def set_to_zero(matrix):
    m, n = len(matrix), len(matrix[0])
    row, column = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)
    for i in range(m):
        for j in range(n):
            if i in row or j in column:
                matrix[i][j] = 0
    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print('-'*3*len(matrix[0]))


if __name__ == '__main__':
    # Test case 0
    matrix0 = [[1, 2, 3, 4],
               [5, 6, 0, 8],
               [9, 10, 0, 12],
               [13, 14, 15, 16]]
    print_matrix(matrix0)
    print_matrix(set_to_zero(matrix0))

    # Test case 1
    matrix1 = [[0, 2, 3],
               [0, 5, 6],
               [7, 8, 9]]
    print_matrix(matrix1)
    print_matrix(set_to_zero(matrix1))

    # Test case 2
    matrix2 = [[1, 2, 3, 4],
               [5, 6, 7, 8]]
    print_matrix(matrix2)
    print_matrix(set_to_zero(matrix2))

    # Test case 3
    matrix3 = [[1, -2, 3],
               [5, 6, 'K'],
               [9, 10, -11],
               ['n', 0, 15]]
    print_matrix(matrix3)
    print_matrix(set_to_zero(matrix3))
