# stack.py


from linked_list import *


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is not None:
            item = self.top.data
            self.top = self.top.next
            return item
        return

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def peek(self):
        return self.top.data
