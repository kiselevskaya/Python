# ascending_order.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        data = Node(data)
        self.size += 1
        data.next = self.top
        self.top = data

    def pop(self):
        if self.top is not None:
            value = self.top.data
            self.top = self.top.next
            self.size -= 1
            return value
        print('Trying to pop an empty stack')
        return

    def peek(self):
        return self.top.data

    def output(self):
        if self.size == 0:
            print('<-', end='  ')
        current = self.top
        while current is not None:
            if current.next is None:
                print(current.data, end='       ')
            else:
                print(current.data, end='<-')
            current = current.next


class AscendingOrder:
    def __init__(self):
        self.main = Stack()
        self.buffer = Stack()

    def push(self, data):
        while not self.is_empty() and self.main.peek() > data:
            self.buffer.push(self.main.pop())
            self.content()
        self.main.push(data)
        self.content()
        while self.buffer.top is not None:
            self.main.push(self.buffer.pop())
            self.content()

    def pop(self):
        self.main.pop()

    def peek(self):
        return self.main.peek()

    def is_empty(self):
        return self.main.size == 0

    def content(self):
        print('Main:', end=' '), self.main.output()
        print('Buffer:', end=' '), self.buffer.output()
        print()


if __name__ == '__main__':
    import random
    test_array = [round(random.random(), 2) for i in range(8)]
    ordered = AscendingOrder()

    print('Test ascending order while push the data\n')
    for i in test_array:
        ordered.push(i)
        print(ordered.peek(), '\n')

    print('Test popping')
    ordered.pop()
    print(ordered.peek())
    ordered.pop()
    print(ordered.peek())

