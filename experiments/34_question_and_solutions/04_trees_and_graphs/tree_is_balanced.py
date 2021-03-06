# tree_is_balanced.py


""" A balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_unbalanced():
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(11)
    root.left.left.left = Node(111)
    root.left.right = Node(12)
    root.right = Node(2)
    root.right.right = Node(21)
    root.right.right.right = Node(22)
    return root


def tree_balanced():
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.left.left = Node(6)
    root.left.right = Node(4)
    root.right = Node(2)
    root.right.right = Node(5)
    return root


# O(N^2)

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right))+1


def tree_is_balanced(root):
    if root is None:
        return True
    height_diff = get_height(root.left)-get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return tree_is_balanced(root.left) and tree_is_balanced(root.right)


# O(N) time, O(log N) space

def height(root):
    if root is None:
        return 0

    left = height(root.left)
    if left == -1:
        return -1

    right = height(root.right)
    if right == -1:
        return -1

    diff = abs(left - right)
    if diff > 1:
        return -1
    else:
        return max(left, right) + 1


def is_balanced(root):
    return False if height(root) == -1 else True


if __name__ == '__main__':
    # test for balanced tree
    assert is_balanced(tree_balanced()) is True, "Should return True as tree is balanced"
    # test for unbalanced tree
    assert is_balanced(tree_unbalanced()) is False, "Should return False as tree is unbalanced"

