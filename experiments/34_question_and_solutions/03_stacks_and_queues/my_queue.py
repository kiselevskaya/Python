# my_queue.py


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
            print('-empty-', end='  ')
        current = self.top
        while current is not None:
            if current.next is None:
                print(current.data, end='  ')
            else:
                print(current.data, end='<-')
            current = current.next


class MyQueue:
    def __init__(self):
        self.newest = Stack()
        self.oldest = Stack()

    def shift(self):
        if self.oldest.size == 0:
            while self.newest.size > 0:
                self.oldest.push(self.newest.pop())

    def enqueue(self, data):
        self.newest.push(data)

    def dequeue(self):
        self.shift()
        return self.oldest.pop()

    def peek(self):
        self.shift()
        self.oldest.peek()

    def content(self):
        print('Newest stack:', end=' '), self.newest.output()
        print('Oldest stack:', end=' '), self.oldest.output()
        print()


if __name__ == '__main__':
    queue = MyQueue()
    for i in range(5):
        queue.enqueue(i)
    queue.content()

    queue.enqueue(5)
    queue.content()

    print(queue.dequeue())
    queue.content()

    print(queue.dequeue())
    queue.content()

    queue.enqueue(6)
    queue.content()

    print(queue.dequeue())
    queue.content()
