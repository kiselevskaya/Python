

import unittest


def sum_of_intervals(intervals):
    lst = []
    for interval in intervals:
        for n in range(interval[0], interval[1]):
            lst.append(n)
    return len(set(lst))


sum_of_intervals([(1, 2), (6, 10), (11, 15)])


class TestSumOfIntervals(unittest.TestCase):

    def test_sum_is_04(self):
        self.assertIs(sum_of_intervals([(1, 5)]), 4)

    def test_sum_is_8(self):
        self.assertIs(sum_of_intervals([(1, 5), (6, 10)]), 8)

    def test_sum_is_4(self):
        self.assertIs(sum_of_intervals([(1, 5), (1, 5)]), 4)

    def test_sum_is_7(self):
        self.assertIs(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

    def test_sum_is_19(self):
        self.assertIs(sum_of_intervals([(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)]), 19)

    def test_sum_is_9(self):
        self.assertIs(sum_of_intervals([(1, 2), (6, 10), (11, 15)]), 9)


if __name__ == '__main__':
    unittest.main()
