# is_binary_search_tree.py


"""
Implement a function to check if binary tree is a binary search tree.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def bst():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.left.left.left = Node(0)
    root.left.left.right = Node(2)
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right = Node(10)
    root.right.right.left = Node(9)
    root.right.right.right = Node(12)
    root.right.right.right.left = Node(11)
    root.right.right.right.right = Node(13)
    return root


def left_equal_root():
    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.left.left.left = Node(0)
    root.left.left.right = Node(2)
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right = Node(10)
    root.right.right.left = Node(9)
    root.right.right.right = Node(12)
    root.right.right.right.left = Node(11)
    root.right.right.right.right = Node(13)
    return root


def right_equal_root():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.left.left = Node(0)
    root.left.left.right = Node(2)
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right = Node(10)
    root.right.right.left = Node(9)
    root.right.right.right = Node(12)
    root.right.right.right.left = Node(11)
    root.right.right.right.right = Node(13)
    return root


def left_bigger_root():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.left.left.left = Node(0)
    root.left.left.right = Node(2)
    root.right.left = Node(9)
    root.right.right = Node(10)
    root.right.right.right = Node(12)
    root.right.right.right.left = Node(11)
    root.right.right.right.right = Node(13)
    return root


def right_smaller_root():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(2)
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right = Node(10)
    root.right.right.left = Node(9)
    root.right.right.right = Node(12)
    root.right.right.right.left = Node(11)
    root.right.right.right.right = Node(13)
    return root


def is_bst(root, order):
    if root is not None:
        # Traverse left
        is_bst(root.left, order)
        # Traverse root
        # print(str(root.data) + "->", end=' ')
        if len(order) == 0 or order[-1] < root.data:
            order.append(root.data)
        else:
            return False
        # Traverse right
        is_bst(root.right, order)
    return True


if __name__ == '__main__':
    order = []
    # Test binary tree is binary search tree
    # print(is_bst(bst(), order))
    assert is_bst(bst(), order) is True, "Binary tree is binary search tree"

    # Test left node equal root
    # print(is_bst(left_equal_root(), order))
    assert is_bst(left_equal_root(), order) is False, "Binary tree is NOT binary search tree"

    # Test right node equal root
    # print(is_bst(right_equal_root(), order))
    assert is_bst(right_equal_root(), order) is False, "Binary tree is NOT binary search tree"

    # Test left bigger than root
    # print(is_bst(left_bigger_root(), order))
    assert is_bst(left_bigger_root(), order) is False, "Binary tree is NOT binary search tree"

    # Test right smaller than root
    # print(is_bst(right_smaller_root(), order))
    assert is_bst(right_smaller_root(), order) is False, "Binary tree is NOT binary search tree"
