

import re
import unittest


def is_interesting(number, awesome_phrases):
    if number < 98:
        return 0
    else:
        def interesting(num):
            lst = list(str(num))
            length = len(lst)//2

            # Any digit followed by all zeros: 100, 90000
            if int(str(num)[0]) in range(1, 10) and num % 10**(len(str(num))-1) == 0:
                return True

            # Every digit is the same number: 1111
            if len(set(str(number))) == 1 and len(lst) > 2:
                return True

            # The digits are a palindrome: 1221 or 73837
            if lst[:length] == lst[-length:][::-1]:
                return True

            # # The digits are sequential, incrementing: 1234
            # for i in range(len(lst)):
            #     try:
            #         if (int(lst[i])+1) % 10 == int(lst[i+1]):
            #             continue
            #         else:
            #             return False
            #     except Exception as e:
            #         print(e)
            #         return True

        # def almost_interesting(num):
        #     pass

        reverse_num = int(''.join(list(str(number))[::-1]))
        if interesting(number) or interesting(reverse_num):
            return 2
        else:
            return 0


class TestCarMileage(unittest.TestCase):

    def test_is_run_negative100(self):
        self.assertIs(is_interesting(-100, []), 0)

    def test_is_run_negative99(self):
        self.assertIs(is_interesting(-99, []), 0)

    def test_is_run_negative98(self):
        self.assertIs(is_interesting(-98, []), 0)

    def test_is_run_zero(self):
        self.assertIs(is_interesting(0, []), 0)

    def test_is_run_50(self):
        self.assertIs(is_interesting(50, []), 0)

    def test_is_run_97(self):
        self.assertIs(is_interesting(97, []), 0)

    def test_is_run_98(self):
        self.assertIs(is_interesting(98, []), 0)

    def test_is_run_99(self):
        self.assertIs(is_interesting(99, []), 2)

    def test_is_run_102(self):
        self.assertIs(is_interesting(102, []), 0)

    def test_is_run_99999(self):
        self.assertIsNot(is_interesting(99999, []), 0)

    #   Any digit followed by all zeros: 100, 90000
    def test_is_run_100(self):
        self.assertIs(is_interesting(100, []), 2)

    def test_is_run_90000(self):
        self.assertIs(is_interesting(90000, []), 2)

    # Every digit is the same number: 1111
    def test_is_run_1111(self):
        self.assertIs(is_interesting(1111, []), 2)

    def test_is_run_9999(self):
        self.assertIs(is_interesting(9999, []), 2)

    # The digits are a palindrome: 1221 or 73837
    def test_is_run_73437(self):
        self.assertIs(is_interesting(73437, []), 2)

    def test_is_run_1221(self):
        self.assertIs(is_interesting(1221, []), 2)

    def test_is_run_124521(self):
        self.assertIsNot(is_interesting(124521, []), 2)

    # # The digits are sequential, incementing: 1234
    # def test_is_run_67890(self):
    #     self.assertIs(is_interesting(67890, []), 2)
    #
    # def test_is_run_1434(self):
    #     self.assertIsNot(is_interesting(1434, []), 2)
    #
    # # The digits are sequential, decrementing: 4321
    # def test_is_run_43210(self):
    #     self.assertIs(is_interesting(43210, []), 2)


if __name__ == '__main__':
    unittest.main()


# The digits match one of the values in the awesome_phrases array


# For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
