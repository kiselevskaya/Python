# alter_pass_most_points.py


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


class Line:
    def __init__(self, point1, point2):
        self.p = point1
        self.q = point2
        self.epsilon = 0.0001
        self.slope = None
        self.infinite_slope = False
        if abs(self.p.x - self.q.x) > self.epsilon:
            self.slope = (self.p.y - self.q.y) / (self.p.x - self.q.x)
            self.intercept = self.p.y - self.slope * self.p.x
        else:
            self.intercept = self.p.x
            self.infinite_slope = True

    def floor_to_nearest_eps(self, slope):
        return slope if slope is None else int(slope/self.epsilon)*self.epsilon

    def is_equivalent(self, a, b):
        if a is None and b is None:
            return True
        return abs(a - b) < self.epsilon

    def equal_line(self, line):
        if (self.is_equivalent(self.slope, line.slope)
                and self.is_equivalent(self.intercept, line.intercept)
                and self.infinite_slope == line.infinite_slope):
            return True
        return False


def insert_line(lines, line):
    key = line.floor_to_nearest_eps(line.slope)
    if key not in lines.keys():
        lines.update({key: []})
    lines[key].append(line)
    return lines


def best_line(points):
    final_line = None
    best_count = 0
    lines = {}
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            line = Line(points[i], points[j])
            lines = insert_line(lines, line)
            count = count_equivalent(lines, line)
            if count > best_count:
                best_count = count
                final_line = line
    return final_line


def count_equivalent(lines, line):
    key = line.floor_to_nearest_eps(line.slope)
    eps = line.epsilon
    count = count_equivalent_lines(lines[key], line)
    if key is not None:
        for k in [key-eps, key+eps]:
            try:
                count += count_equivalent_lines(lines[k], line)
            except KeyError:
                pass
    return count


def count_equivalent_lines(lines, line):
    if not bool(lines):
        return 0
    count = 0
    for parallel in lines:
        if parallel.equal_line(line):
            count += 1
    return count


if __name__ == '__main__':
    data = [Point(3, -2), Point(-2, -2), Point(-2, 2), Point(4, 4), Point(1, 1), Point(2, -3)]
    print(best_line(data))
