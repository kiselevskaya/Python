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

    # def shift(self, index):
    #     stack = self.stacks[index]
    #     return

    # def pop_at(self, index):
    #     print('{} popped from stack {}'.format(self.stacks[index].pop(), index))
    #     if self.stacks[index].top is None:
    #         print('Stack {} is empty'.format(index))
    #         self.stacks.pop(index)
    #         return
    #     if len(self.stacks)-1 <= index+1:
    #         self.shift(index+1)

    def peek(self):
        try:
            return self.stacks[self.index].peek()
        except Exception as e:
            print(e)
            return


if __name__ == '__main__':
    stacks = SetOfStacks()
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.push(6)
    stacks.push(7)
    stacks.push(8)
    stacks.push(9)
    stacks.push(10)
    stacks.push(11)
    # stacks.pop_at(1)
    # stacks.pop_at(0)
    # stacks.pop_at(0)
    # stacks.pop_at(0)
    # stacks.pop_at(0)


