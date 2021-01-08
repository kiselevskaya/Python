# stack_with_min.py


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def append(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        data.next = self.top
        self.top = data

    def delete(self):
        try:
            self.top = self.top.next
        except Exception as e:
            print(e)

    def get_top(self):
        return self.top.data


class StackWithMin(Stack):

    def __init__(self):
        super().__init__()
        self.min = Stack()

    def push(self, value):
        if self.min.top is None or value < self.min.top.data:
            self.min.append(value)
        super().append(value)

    def pop(self):
        if super().get_top() == self.min.top.data:
            self.min.delete()
        super().delete()

    def peek(self):
        return super().get_top()

    def minimum(self):
        return self.min.get_top()


if __name__ == '__main__':
    stack_with_min = StackWithMin()

    stack_with_min.push(5)      # 5, 5, 5
    print('Pushed 5, top {}, min {}'.format((stack_with_min.peek()), (stack_with_min.minimum())))

    stack_with_min.push(6)      # 6, 6, 5
    print('Pushed 6, top {}, min {}'.format((stack_with_min.peek()), (stack_with_min.minimum())))

    stack_with_min.push(3)      # 3, 3, 3
    print('Pushed 3, top {}, min {}'.format((stack_with_min.peek()), (stack_with_min.minimum())))

    stack_with_min.push(7)      # 7, 7, 3
    print('Pushed 7, top {}, min {}'.format((stack_with_min.peek()), (stack_with_min.minimum())))

    stack_with_min.pop()      # 3, 3
    print('Poped last(7), top {}, min {}'.format((stack_with_min.peek()), (stack_with_min.minimum())))

    stack_with_min.pop()      # 5, 5
    print('Poped last(3), top {}, min {}'.format((stack_with_min.peek()), (stack_with_min.minimum())))


