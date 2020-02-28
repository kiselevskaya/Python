

import unittest


def pattern_to_number(pattern):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    n = len(pattern)
    for i in range(len(pattern)):
        number += order[pattern[i]]*4**(n-1-i)
    return number


def number_to_pattern(number, k):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    pattern = ''
    dividend = number
    for i in range(k):
        pattern = list(order.keys())[list(order.values()).index(dividend % 4)] + pattern
        dividend = dividend // 4
    return pattern


class TestPatternToNumberAndBack(unittest.TestCase):

    def test_pattern_to_number(self):
        pattern = 'ATGCAA'
        number = 912
        self.assertEqual(pattern_to_number(pattern), number)

    def test_number_to_pattern_0(self):
        number = 912
        k = 6
        pattern = 'ATGCAA'
        self.assertEqual(number_to_pattern(number, k), pattern)

    def test_number_to_pattern_1(self):
        number = 5437
        k = 7
        pattern = 'CCCATTC'
        self.assertEqual(number_to_pattern(number, k), pattern)

    def test_number_to_pattern_2(self):
        number = 5437
        k = 8
        pattern = 'ACCCATTC'
        self.assertEqual(number_to_pattern(number, k), pattern)


if __name__ == '__main__':
    unittest.main()
