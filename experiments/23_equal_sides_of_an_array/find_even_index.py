

array = [1,2,3,4,5,6]
print("answer is: index = -1")


def find_even_index(array):
    print("origin: ", array, "len: ", len(array))
    sum_origin = list((sum(array[:i])) for i in range(len(array)+1))
    print("sum of origin: ", sum_origin, "len: ", len(sum_origin))
    sum_inversion = list((sum(array[::-1][:i])) for i in range(len(array)+1))
    print("sum of inversion: ", sum_inversion, "len: ", len(sum_inversion))

    indexes = []
    outs = []
    for i in range(len(sum_origin)):
        if sum_origin[i] in sum_inversion:
            equals = [index for index, value in enumerate(sum_inversion) if value == sum_origin[i]]
            indexes.append(equals)
            for index in equals:
                if index + i + 1 == len(array):
                    outs.append(i)

    print("output: ", outs)
    if len(outs) != 0:
        print(outs[0])
        return outs[0]
    else:
        print(-1)
        return -1


find_even_index(array)

# array = [3, 70, 9, -7, 2, -7, 12, 9, -1, 8, -14, 11, 3, 3, 51]
# [0, 3, 73, 82, 75,      77, 70, 82, 91, 90, 98, 84, 95, 98, 101]
# [0, 51, 54, 57, 68, 54, 62, 61, 70, 82, 75,    77,  70, 79, 149] -3
# It should work for random inputs too: 6 should equal 4

# array = [29, -18, 0, 18, 15, 0, 1, -19, 18, -11, 15, -8]
# It should work for random inputs too: 3 should equal 1

# array = [-19, -15, -8, 18, -1, 53, 19, -12, 18, -16, 7, -6, -19, 19, -8, -16, 5, 20, -6, 18, 18, 7, -1, 19, 6, -12, 4, -5, -15, 10]
# It should work for random inputs too: 11 should equal 7
