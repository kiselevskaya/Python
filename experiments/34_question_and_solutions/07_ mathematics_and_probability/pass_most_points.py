# pass_most_points.py


"""
Given a two-dimensional graph with points on it, find a line which passes the most number of points.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def point(self):
        return self.x, self.y


def best_line(points):
    # Dictionary for each slope as key and all lines between any 2 pints with this slope as value
    slopes = {}
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            slope = None if (points[i].x - points[j].x) == 0 else (points[i].y - points[j].y) / (points[i].x - points[j].x)
            line = points[i].point(), points[j].point()
            try:
                slopes[slope].append(line)
            except KeyError:
                slopes[slope] = [line]
    # The most frequent slope first
    slopes = sorted(slopes.items(), key=lambda x: len(x[1]), reverse=True)
    # Finds if lines pass more than through 2 points and returns the longest one, line determines by all points it passes
    current = 0
    result = []
    while current < len(slopes):
        if len(result) >= len(slopes[current][1]):
            return result
        max_line = connect_lines(slopes[current][1])
        if len(max_line) > len(result):
            result = max_line
        current += 1
    return result


def connect_lines(lines):
    line = None
    for i in range(len(lines)):
        l = list(lines[i])
        for j in range(1, len(lines)):
            k = (i+j) % len(lines)
            if list(lines[k])[0] in l or list(lines[k])[0] in l:
                l.extend(list(lines[k]))
        if line is None or len(l) > len(line):
            line = l
    result = list(set(line))
    return result


if __name__ == '__main__':
    data = [Point(3, -2), Point(-2, -2), Point(-2, 2), Point(4, 4), Point(1, 1), Point(2, -3)]
    output = [(1, 1), (4, 4), (-2, -2)]
    assert sorted(best_line(data)) == sorted(output), 'Test 1 line through 3 points: (-2, -2), (1, 1), (4, 4)'
