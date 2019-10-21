

import unittest
from catching_car_mileage_number import is_interesting


class TestCarMileage(unittest.TestCase):

    def test_run_negative100(self):
        self.assertIs(is_interesting(-100, []), 0)

    def test_run_negative99(self):
        self.assertIs(is_interesting(-99, []), 0)

    def test_run_negative98(self):
        self.assertIs(is_interesting(-98, []), 0)

    def test_run_zero(self):
        self.assertIs(is_interesting(0, []), 0)

    def test_run_50(self):
        self.assertIs(is_interesting(50, []), 0)

    def test_run_97(self):
        self.assertIs(is_interesting(97, []), 0)

    def test_run_98(self):
        self.assertIs(is_interesting(98, []), 1)

    def test_run_99(self):
        self.assertIs(is_interesting(99, []), 1)

    def test_run_102(self):
        self.assertIs(is_interesting(102, []), 0)

    def test_run_99999(self):
        self.assertIs(is_interesting(99999, []), 2)

    #   Any digit followed by all zeros: 100, 90000
    def test_run_100(self):
        self.assertIs(is_interesting(100, []), 2)

    def test_run_90000(self):
        self.assertIs(is_interesting(90000, []), 2)

    # Every digit is the same number: 1111
    def test_run_1111(self):
        self.assertIs(is_interesting(1111, []), 2)

    def test_run_9999(self):
        self.assertIs(is_interesting(9999, []), 2)

    # The digits are a palindrome: 1221 or 73837
    def test_run_73437(self):
        self.assertIs(is_interesting(73437, []), 2)

    def test_run_1221(self):
        self.assertIs(is_interesting(1221, []), 2)

    def test_run_124521(self):
        self.assertIs(is_interesting(124521, []), 0)

    # # The digits are sequential, incrementing: 1234
    # For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
    def test_run_67890(self):
        self.assertIs(is_interesting(67890, []), 2)

    def test_run_3456(self):
        self.assertIs(is_interesting(3456, []), 2)

    def test_run_89012(self):
        self.assertIs(is_interesting(78901, []), 0)

    # The digits are sequential, decrementing: 4321
    # For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
    def test_run_43210(self):
        self.assertIs(is_interesting(43210, []), 2)

    def test_run_8765(self):
        self.assertIs(is_interesting(8765, []), 2)

    def test_run_21098(self):
        self.assertIs(is_interesting(32109, []), 0)


if __name__ == '__main__':
    unittest.main()
