import math
def polygon_area(siges, length):
    return (siges * (length ** 2)) / (4 * math.tan(math.pi / siges))

#print polygon_area(7, 3)
print polygon_area(5, 7)
