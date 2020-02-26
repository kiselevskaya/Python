

import unittest


# is case sensitive or space sensitive?

#   O(n^2)
def string_permutation(string, another):
    if len(string) != len(another):
        return False

    sorted_string = ''.join(sorted(list(string.lower())))
    sorted_another = ''.join(sorted(list(another.lower())))

    for i in range(len(string)):
        if sorted_string[i] != sorted_another[i]:
            return False
    return True


#   O(n log n)
def string_permutation_log_n(string, another):
    if len(string) != len(another):
        return False

    count_string = [0]*256
    count_another = [0]*256

    for i in range(len(string)):
        count_string[ord(string.lower()[i])] += 1

    for j in range(len(another)):
        count_another[ord(another.lower()[j])] += 1

    for n in range(len(count_string)):
        if count_string[n] != count_another[n]:
            return False

    return True


class TestStringPermutation(unittest.TestCase):

    def test_string_permutation(self):
        a = string_permutation('dog', 'God')
        self.assertIs(a, True)

    def test_string_permutation_fail(self):
        a = string_permutation('dog ', 'God')
        self.assertIsNot(a, True)

    def test_string_permutation_2(self):
        a = string_permutation('Cat', 'God')
        self.assertIs(a, False)

    def test_string_permutation_log_n(self):
        a = string_permutation('dog', 'God')
        self.assertIs(a, True)

    def test_string_permutation_log_n_fail(self):
        a = string_permutation('dog ', 'God')
        self.assertIsNot(a, True)

    def test_string_permutation_log_n_2(self):
        a = string_permutation('Cat', 'God')
        self.assertIs(a, False)


if __name__ == '__main__':
    unittest.main()
