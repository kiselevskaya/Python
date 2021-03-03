# cut_squares_in_half.py


"""
Given two squares on a two-dimensional plane, find a line that would cut these two squares in half.
Assume that the top and the bottom of the square run parallel to the x-axis.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y


class Square:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.mid = Point((self.right+self.left)/2, (self.top+self.bottom)/2)

    def middle_line(self):
        return Point(self.mid.x, self.bottom.y), Point(self.mid.x, self.top.y)

    def extend(self, mid1, mid2, size):
        x_dir = -1 if mid1.x < mid2.x else 1
        y_dir = -1 if mid1.y < mid2.y else 1

        if mid2.x == mid1.x:
            return Point(mid1.x, mid1.y + y_dir * size / 2)

        slope = (mid2.y - mid1.y) / (mid2.x - mid1.x)

        if abs(slope) == 1:
            x1 = mid1.x + x_dir * size / 2
            y1 = mid1.y + y_dir * size / 2
            return Point(x1, y1)
        elif abs(slope) < 1:
            x1 = mid1.x + x_dir * size / 2
            y1 = slope * (x1 - mid1.x) + mid1.y
            return Point(x1, y1)
        else:
            y1 = mid1.y + y_dir * size / 2
            x1 = (y1-mid1.y) / slope + mid1.x
            return Point(x1, y1)

    def line(self, other):
        if self.mid == other.mid:
            bigger = self if (self.top-self.bottom) > (other.top-other.bottom) else other
            return Point(bigger.mid.x, bigger.bottom), Point(bigger.mid.x, bigger.top)
        point1 = self.extend(self.mid, other.mid, self.right-self.left)
        point2 = self.extend(other.mid, self.mid, other.right-other.left)
        return point1, point2


if __name__ == '__main__':
    # left, right, top, bottom
    sq1 = Square(0, 2, 2, 0)
    sq2 = Square(5, 6, 4, 3)

    line = sq1.line(sq2)
    print([point.get_point() for point in line])
