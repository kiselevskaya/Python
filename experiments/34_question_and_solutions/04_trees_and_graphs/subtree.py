# subtree.py


"""
There are two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
Decide if T2 is a subtree of T1.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None


def t1():
    r = Node(8)
    r.left = Node(2)
    r.right = Node(7)
    r.left.left = Node(98)
    r.right.left = Node(5)
    r.right.right = Node(11)
    r.left.left.left = Node(0)
    r.left.left.right = Node(56)
    r.right.left.right = Node(17)
    r.right.left.left = Node(39)
    return r


def t2():
    r = Node(2)
    r.left = Node(98)
    r.left.left = Node(0)
    r.left.right = Node(56)
    return r


def t3():
    r = Node(7)
    r.left = Node(5)
    r.right = Node(11)
    r.left.left = Node(39)
    r.left.right = Node(17)
    return r


def t4():
    r = Node(5)
    r.left = Node(39)
    r.right = Node(17)
    return r


def t5():
    r = Node(7)
    r.left = Node(5)
    r.right = Node(11)
    return r


def t6():
    r = Node(8)
    r.left = Node(2)
    r.left.left = Node(98)
    r.left.left.left = Node(0)
    r.left.left.right = Node(56)
    return r


# Solution

def subtree(root1, root2):
    if root2 is None:       # tree always contain an empty subtree
        return True
    return contains(root1, root2)       # pre-order to compare: root -> left -> right


def contains(r1, r2):
    if r1 is None:      # empty subtree can not contain any subtree
        return False
    if r1.data == r2.data:      # if node data matches tree2 root compare subtrees
        if compare(r1, r2):     # return True if subtrees are equal
            return True
    return subtree(r1.left, r2) or subtree(r1.right, r2)


def compare(r1, r2):
    if r1 is None and r2 is None:   # nothing left to compare and all previous nodes match
        return True
    if r1 is None or r2 is None:    # if node of any subtree to compare is None
        return False
    if r1.data != r2.data:      # stop comparison as nodes don't match each other
        return False
    return compare(r1.left, r2.left) and compare(r1.right, r2.right)    # if all before matches continue to compare recursively


if __name__ == '__main__':
    # Test 1
    #             8           None
    #           /    \
    #          2      7
    #         /      / \
    #       98      5   11
    #      /  \    / \
    #     0   56  39  17
    assert subtree(t1(), None) is True, 'Test 1: True expected'

    # Test 2
    #   None        5
    #              / \
    #             39  17
    assert subtree(None, t4()) is False, 'Test 2: True expected'

    # Test 3
    #             8                  2
    #           /    \              /
    #          2      7           98
    #         /      / \         /  \
    #       98      5   11      0   56
    #      /  \    / \
    #     0   56  39  17
    assert subtree(t1(), t2()) is True, 'Test 3: True expected'

    # Test 4
    #             8                  7
    #           /    \              / \
    #          2      7            5   11
    #         /      / \          / \
    #       98      5   11       39  17
    #      /  \    / \
    #     0   56  39  17
    assert subtree(t1(), t3()) is True, 'Test 4: True expected'

    # Test 5
    #             8                5
    #           /    \            / \
    #          2      7         39   17
    #         /      / \
    #       98      5   11
    #      /  \    / \
    #     0   56  39  17
    assert subtree(t1(), t4()) is True, 'Test 5: True expected'

    # Test 6
    #             8                7
    #           /    \            / \
    #          2      7          5   11
    #         /      / \
    #       98      5   11
    #      /  \    / \
    #     0   56  39  17
    assert subtree(t1(), t5()) is False, 'Test 6: False expected'

    # Test 57
    #             8                  8
    #           /    \              /
    #          2      7            2
    #         /      / \          /
    #       98      5   11       98
    #      /  \    / \          /  \
    #     0   56  39  17       0   56
    assert subtree(t1(), t6()) is False, 'Test 5: False expected'
