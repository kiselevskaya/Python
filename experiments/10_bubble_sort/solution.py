#lst = [23, -1, 64, 0, 88, 7, 8.3]
lst = list(range(1001))
lst.reverse()
def bubble(massif):
    length = len(massif) - 1
    sorted = False
    count = 0

    while not sorted:
        sorted = True
        for i in range(length):
            if massif[i] > massif[i+1]:
                sorted = False
                massif[i], massif[i+1] = massif[i+1], massif[i]
                count += 1

    return massif, count

print (bubble(lst))
