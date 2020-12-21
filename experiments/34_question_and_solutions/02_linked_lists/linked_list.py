# 01_remove_duplicates.py


class Node:
    def __init__(self, data=None):
        self.data = data    # stores node data
        self.next = None    # stores reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):     # adds new node to the end of list
        if not isinstance(data, Node):
            data = Node(data)

        if self.head is None:
            self.head = data
        else:
            self.tail.next = data

        self.tail = data

    def length(self):   # counts the number of nodes in list returns integer
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total

    def output(self):   # prints all nodes values
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
