

import unittest


def string_compression(string):
    # is string ASCII or Unicode
    length = len(string)
    new_length = 0
    compresed = ''
    count = 0
    for i in range(length):
        char = string[i]
        count += 1
        try:
            if string[i] != string[i+1]:
                compresed += char+str(count)
                new_length += 1+len(str(count))
                count = 0
        except Exception as e:
            print(e)
            compresed += char+str(count)
            new_length += 1+len(str(count))
        if new_length >= length:
            return string
    return compresed


class TestStringCompression(unittest.TestCase):

    def test_string_compression(self):
        a = string_compression('aabcccccaaa')
        b = 'a2b1c5a3'
        self.assertEqual(a, b)

    def test_string_compression2(self):
        a = string_compression('abca')
        b = 'a1b1c1a1'
        c = 'abca'
        self.assertNotEqual(a, b)
        self.assertEqual(a, c)


if __name__ == '__main__':
    unittest.main()
