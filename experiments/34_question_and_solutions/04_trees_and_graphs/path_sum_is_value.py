# path_sum_is_value.py


"""
Design an algorithm to print all paths of binary tree which sum to a given value.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None


def tree():
    r = Node(8)
    r.left = Node(2)
    r.right = Node(7)
    r.left.left = Node(98)
    r.right.left = Node(-5)
    r.right.right = Node(11)
    r.left.left.left = Node(0)
    r.left.left.right = Node(-56)
    r.right.left.right = Node(18)
    r.right.left.left = Node(39)
    return r


def sum_path(root, value, arr, output):
    if root is None:
        return
    arr.append(root.data)
    sum_path(root.left, value, arr, output)
    sum_path(root.right, value, arr, output)
    if sum(arr) == value:
        print('Sum', value, arr)
        output.append(list(arr))
    arr.pop()


def wrap(root, value, output):
    if root is None:
        return
    arr = []
    sum_path(root, value, arr, output)
    wrap(root.left, value, output)
    wrap(root.right, value, output)
    return output


def path_sum_value(root, value):
    if value is None or root is None:
        return
    output = []
    output = wrap(root, value, output)
    return output[0] if len(output) < 2 else output


if __name__ == '__main__':
    #              8
    #           /     \
    #          2       7
    #         /       / \
    #       98      -5   11
    #      /  \     / \
    #     0   -56  39  18

    # Test 1
    assert path_sum_value(tree(), 0) == [0], 'Test 1: [0] expected'

    # # Test 2
    assert path_sum_value(tree(), 10) == [[8, 2], [8, 7, -5]], 'Test 2: {} expected'.format([[8, 2], [8, 7, -5]])

    # # Test 3
    assert path_sum_value(tree(), 13) == [-5, 18], 'Test 3: {} expected'.format([-5, 18])
