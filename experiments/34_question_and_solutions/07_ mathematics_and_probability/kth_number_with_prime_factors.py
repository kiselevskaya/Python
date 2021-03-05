# kth_number_with_prime_factors.py


"""
Design algorithm to find the kth number such that the only prime factors are 3, 5, 7.
"""


import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        return self.head if self.head is None else self.head.value


def kth_number(k):
    q3 = LinkedList()
    q5 = LinkedList()
    q7 = LinkedList()
    q3.add(Node(1))
    value = None
    for i in range(k+1):
        v3 = sys.maxsize if q3.peek() is None else q3.peek()
        v5 = sys.maxsize if q5.peek() is None else q5.peek()
        v7 = sys.maxsize if q7.peek() is None else q7.peek()
        value = min(v3, v5, v7)
        if value == v3:
            q3.pop()
            q3.add(Node(3*value))
            q5.add(Node(5*value))
        elif value == v5:
            q5.pop()
            q5.add(Node(5*value))
        else:
            q7.pop()
        q7.add(Node(7*value))
    return value


if __name__ == '__main__':
    print(kth_number(5))

