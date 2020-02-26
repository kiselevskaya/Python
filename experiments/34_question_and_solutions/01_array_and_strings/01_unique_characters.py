

import unittest


#   O(n)
def unique_characters_n(string):
    # is string ASCII or Unicode
    if len(string) > 256:
        return False

    chars = [False]*128
    for i in range(len(string)):
        if chars[ord(string[i])]:
            return False
        else:
            chars[ord(string[i])] = True
    return True


#   O(n^2)
def unique_characters_sqrt_n(string):
    # is string ASCII or Unicode
    if len(string) > 256:
        return False

    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


#   O(n log n)
# def unique_characters_n_log_n(string):
#     # is string ASCII or Unicode
#     if len(string) > 256:
#         return False


class TestUniqueCharacters(unittest.TestCase):

    def test_unique_characters_n(self):
        a = unique_characters_n('asdfghjkd')
        self.assertIs(a, False)

    def test_unique_characters_sqrt_n(self):
        a = unique_characters_sqrt_n('abcertyuiop')
        self.assertIs(a, True)


if __name__ == '__main__':
    unittest.main()
