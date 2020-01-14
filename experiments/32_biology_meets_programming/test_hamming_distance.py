

import unittest
from hamming_distance import *


class TestCarMileage(unittest.TestCase):

    def test_hamming_distance(self):
        self.assertEqual(hamming_distance('GGGCCGTTGGT', 'GGACCGTTGAC'), 3)

    def test_approximate_pattern_matching(self):
        self.assertEqual(approximate_pattern_matching('CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', 'ATTCTGGA', 3), [6, 7, 26, 27])

    def test_approximate_pattern_count(self):
        self.assertEqual(approximate_pattern_count('TTTAGAGCCTTCAGAGG', 'GAGG', 2), 4)


if __name__ == '__main__':
    unittest.main()
