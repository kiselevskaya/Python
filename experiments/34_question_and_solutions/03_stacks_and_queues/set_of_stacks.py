# set_of_stacks.py


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self, capacity=3):
        self.top = None
        self.size = 0
        self.capacity = capacity

    def push(self, data):
        data = Node(data)
        self.size += 1
        data.next = self.top
        self.top = data

    def pop(self):
        if self.top is None:
            print('Trying to pop an empty stack')
            return
        self.size -= 1
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        return self.top.data

    def output(self):
        current = self.top
        while current is not None:
            if current.next is None:
                print(current.data, end='   ')
            else:
                print(current.data, end='->')
            current = current.next


class SetOfStacks:

    def __init__(self):
        self.stacks = [Stack()]
        self.index = 0

    def extend_set(self):
        print('Added new stack into set')
        self.index += 1
        self.stacks.append(Stack())

    def push(self, data):
        if self.stacks[self.index].size == self.stacks[self.index].capacity:
            print('Stack {} reached the capacity'.format(self.index))
            self.extend_set()
        self.stacks[self.index].push(data)
        print('{} pushed to stack {}'.format(data, self.index))

    def pop(self):
        print('{} popped from stack {}'.format(self.stacks[self.index].pop(), self.index))
        if self.stacks[self.index].top is None:
            print('Stack {} is empty'.format(self.index))
            self.stacks.pop()
            self.index -= 1

    def peek(self):
        try:
            return self.stacks[self.index].peek()
        except Exception as e:
            print(e)
            return

    def print_stack(self, index):
        return self.stacks[index].output()

    def shift(self, index, node):
        if node.next is None:
            self.stacks[index-1].push(node.data)
            if self.stacks[index].size == 1:
                self.stacks.pop(index)
            else:
                self.stacks[index].size -= 1
                self.stacks[index].top = self.stacks[index].top.next
            return
        else:
            value = node.data
            self.shift(index, node.next)
            node.next.data = value
        return

    def pop_at(self, index):
        print('{} popped from stack {}'.format(self.stacks[index].pop(), index))
        if self.stacks[index].top is None:
            print('Stack {} is empty'.format(index))
            self.stacks.pop(index)
            return
        while index+1 <= len(self.stacks)-1:
            index += 1
            self.shift(index, self.stacks[index].top)


def represent(set_of_stacks):
    length = len(set_of_stacks.stacks)
    print('Number of stacks ', length)
    for i in range(length):
        set_of_stacks.print_stack(i)
    print()


if __name__ == '__main__':
    stacks = SetOfStacks()
    for i in range(16):
        stacks.push(i)
    represent(stacks)

    stacks.pop_at(0)
    represent(stacks)
