

import unittest


def replace_mid_spaces(string):
    output = ''
    length = len(string)
    # space_count = 0
    # for i in range(length):
    #     if string[i] == " ":
    #         space_count += 1
    # new_length = length + space_count*2

    for j in range(length-1, -1, -1):
        if string[j] == ' ':
            output = '%20'+output
        else:
            output = string[j]+output
    output = output[:length]
    return output


class TestReplaceSpaces(unittest.TestCase):

    def test_replace_mid_spaces(self):
        a = replace_mid_spaces('Mr John Smith    ')
        b = 'Mr%20John%20Smith'
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()

