

'''Given an image represented by an NxM matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degree.
    Let N be image width, M - image height
'''


def rotate_image_clockwise(matrix, clockwise=True):
    n, m = len(matrix), len(matrix[0])
    # Rotate image
    if clockwise:
        # Column of pixels by column
        # For rotate image by 90 degree clockwise left image side (column 0) is going to be on top (row 0)
        # so the first pixel of last row will be the first pixel in the first row etc.
        matrix = [[matrix[j-1][i] for j in range(n, 0, -1)] for i in range(m)]
    else:
        # Row of pixels by row
        matrix = [[matrix[j][i] for j in range(n)] for i in range(m)][::-1]
    return matrix


def create_matrix(n=4, m=4):
    import string
    # Alphabet string
    alpha = string.ascii_uppercase
    # Create template matrix for image (represented as nested list)
    matrix = [[alpha[j] for j in range(i*n, n*(i+1))] for i in range(m)]
    return matrix


def represent_image(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print('-'*2*len(matrix[0]))


'''Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degree.
'''


# Suggested solution (anti-clockwise)
# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
def rotateMatrix(mat, N=4):
    # Consider all squares one by one
    for x in range(0, int(N / 2)):
        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):
            # store current cell in temp variable
            temp = mat[x][y]
            # move values from right to top
            mat[x][y] = mat[y][N-1-x]
            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
            # assign temp to left
            mat[N-1-y][x] = temp


if __name__ == '__main__':
    # Test case 0
    matrix = create_matrix(4, 4)
    represent_image(matrix)
    rotated = rotate_image_clockwise(matrix)
    represent_image(rotated)

    # Test case 1
    matrix1 = create_matrix(2, 4)
    represent_image(matrix1)
    rotated = rotate_image_clockwise(matrix1)
    represent_image(rotated)

    # Test case 2
    matrix2 = create_matrix(5, 2)
    represent_image(matrix2)
    rotated = rotate_image_clockwise(matrix2)
    represent_image(rotated)

    # Test case 3
    matrix3 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
    represent_image(matrix3)
    rotated = rotate_image_clockwise(matrix3, False)
    represent_image(rotated)

    # Test case 4
    matrix4 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    represent_image(matrix4)
    rotated = rotate_image_clockwise(matrix4, False)
    represent_image(rotated)

    # Test case 5
    matrix5 = [[1, 2],
               [4, 5]]
    represent_image(matrix5)
    rotated = rotate_image_clockwise(matrix5, False)
    represent_image(rotated)

    # Test case 6
    matrix6 = [[1, 2, 3],
               [5, 6, 7],
               [9, 10, 11],
               [13, 14, 15]]
    represent_image(matrix6)
    rotated = rotate_image_clockwise(matrix6, False)
    represent_image(rotated)

    # Test case 7
    matrix7 = [[1, 2, 3, 4],
               [5, 6, 7, 8]]
    represent_image(matrix7)
    rotated = rotate_image_clockwise(matrix7, False)
    represent_image(rotated)
