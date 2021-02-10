# common_ancestor.py


"""
Find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.
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
    tree = Tree(45)
    tree.add_child(10, tree.root, 0)
    tree.add_child(3, tree.root, 1)
    tree.add_child(5, tree.root.left, 0)
    tree.add_child(24, tree.root.left, 1)
    tree.add_child(52, tree.root.left.right, 1)
    tree.add_child(198, tree.root.right, 0)
    tree.add_child(1, tree.root.right, 1)
    tree.add_child(6, tree.root.right.right, 1)
    return tree.root


def common_ancestor(root, p, q):
    if root is None:
        return
    if p == root or q == root:
        return root.data
    p_on_left = on_side(root.left, p)
    q_on_left = on_side(root.left, q)

    if p_on_left != q_on_left:
        return root.data

    side = root.left if p_on_left else root.right
    return common_ancestor(side, p, q)


def on_side(side_root, node):
    if side_root is None:
        return False
    if side_root == node:
        return True
    return on_side(side_root.left, node) or on_side(side_root.right, node)


if __name__ == '__main__':
    root = create_tree()
    #           45
    #         /     \
    #       10       3
    #      /  \     |  \
    #     5   24   198  1
    #           \        \
    #           52        6

    # p = 52 q = 198
    assert common_ancestor(root, root.left.right.right, root.right.left) == 45, '45 expected'
    # p = 1 q = 6
    assert common_ancestor(root, root.right.right, root.right.right.right) == 1, '1 expected'
    # p = 198 q = 6
    assert common_ancestor(root, root.right.left, root.right.right.right) == 3, '3 expected'
