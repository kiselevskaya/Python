

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]


def snail(array):
    y, x = 0, 0
    result = []
    if len(array[y]) == 0:
        return result
    elif len(array[y])==1:
        result.append(array[y][x])
    else:
        step = array[y][x]
        result.append(step)
        array[y][x] = 0
        while array[y][x+1] > 0:
            while x < len(array[y])-1 and array[y][x+1] > 0:
                x += 1
                result.append(array[y][x])
                array[y][x] = 0
            while y < len(array)-1 and array[y+1][x] > 0:
                y += 1
                result.append(array[y][x])
                array[y][x] = 0
            while array[y][x-1] > 0:
                x -= 1
                result.append(array[y][x])
                array[y][x] = 0
            while array[y-1][x] > 0:
                y -= 1
                result.append(array[y][x])
                array[y][x] = 0
    print(result)
    print(array)
    return result


snail(array) # => [1,2,3,6,9,8,7,4,5]
