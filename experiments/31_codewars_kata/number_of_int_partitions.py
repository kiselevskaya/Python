

import unittest


def partitions(n):
    parts = [1]+[0]*n
    for t in range(1, n+1):
        for i, x in enumerate(range(t, n+1)):
            parts[x] += parts[i]
    return parts[n]


class TestPartitions(unittest.TestCase):

    def test_1(self):
        self.assertEqual(partitions(1), 1)

    def test_5(self):
        self.assertEqual(partitions(5), 7)

    def test_10(self):
        self.assertEqual(partitions(10), 42)

    def test_25(self):
        self.assertEqual(partitions(25), 1958)


if __name__ == '__main__':
    unittest.main()


# def partitions(n):
#     def partition(n):
#         answer = set()
#         answer.add((n, ))
#         for x in range(1, n):
#             for y in partition(n - x):
#                 answer.add(tuple(sorted((x, ) + y)))
#         return answer
#     return len(partition(n))
# !!! Execution Timed Out

# import math
# def partitions(k):
#     return int(math.exp(math.pi*math.sqrt(2.0*k/3.0))/(4.0*k*math.sqrt(3.0)))

