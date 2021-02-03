# list_for_each_depth.py


"""
Algorithm which creates a linked list of all the nodes at each depth of binary tree.
"""


import queue


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = None

    def add(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def output(self):
        current = self.top
        while current is not None:
            if current.next is None:
                print(current.data, end='  ')
            else:
                print(current.data, end=' <- ')
            current = current.next


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree():
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(2)
    root.left.left.left = Node(3)
    root.left.right = Node(4)
    root.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)
    return root


def enqueue(q, lists):
    if q.empty():
        return
    new_list = LinkedList()
    q1 = queue.Queue()
    while not q.empty():
        node = q.get()
        new_list.add(node.data)
        if node.left is not None:
            q1.put(node.left)
        if node.right is not None:
            q1.put(node.right)
    lists.append(new_list)
    enqueue(q1, lists)
    return


def depth_lists(root):
    q = queue.Queue()
    q.put(root)
    lists = []
    enqueue(q, lists)
    return lists


if __name__ == '__main__':
    root = tree()
    for i in depth_lists(root):
        i.output()
