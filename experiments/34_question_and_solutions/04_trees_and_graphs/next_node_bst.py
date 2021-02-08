# next_node_bst.py


"""
Algorithm to find the 'next' node (i.e., in-order successor) of a given node in a binary search tree.
Assumed that each node has a link to its parent.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.parent = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    # 0 - left, 1 - right
    def add_child(self, data, node, side=None):
        if side == 0:
            node.left = Node(data)
            node.left.parent = node
        elif side == 1:
            node.right = Node(data)
            node.right.parent = node


def create_tree():
    tree = Tree(20)
    tree.add_child(10, tree.root, 0)
    tree.add_child(30, tree.root, 1)
    tree.add_child(5, tree.root.left, 0)
    tree.add_child(15, tree.root.left, 1)
    tree.add_child(25, tree.root.right, 0)
    tree.add_child(35, tree.root.right, 1)
    return tree.root


def inorder_successor(node):
    if node is None:
        return
    if node.parent is None or node.right is not None:
        # return the left most node
        return left_most_node(node.right)
    else:
        # go up
        while node.parent is not None and node == node.parent.right:
            node = node.parent
        return None if node.parent is None else node.parent.data


def left_most_node(node):
    if node is None:
        return None
    while node.left:
        node = node.left
    return node.data


if __name__ == '__main__':
    root = create_tree()

    #        20
    #      /    \
    #    10      30
    #   /  \    /  \
    #  5   15  25  35

    assert inorder_successor(root) == 25, "Should be 25"
    assert inorder_successor(root.left) == 15, "Should be 15"
    assert inorder_successor(root.right) == 35, "Should be 15"
    assert inorder_successor(root.left.left) == 10, "Should be 10"
    assert inorder_successor(root.left.right) == 20, "Should be 20"
    assert inorder_successor(root.right.left) == 30, "Should be 30"
    assert inorder_successor(root.right.right) is None, "Should be None"
