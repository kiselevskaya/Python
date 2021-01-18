# tower_of_hanoi.py


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
        if self.top is None:
            print('Trying to pop an empty stack')
            return
        value = self.top.data
        self.size -= 1
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
                print(current.data, end='<-')
            current = current.next


class TowerOfHanoi:
    def __init__(self, n):
        self.floors = [i for i in range(n)][::-1]
        self.first = Stack()
        for floor in self.floors:
            self.first.push(floor)
        self.towers = [self.first, Stack(), Stack()]
        self.steps = 0

    def step(self):
        self.steps += 1
        print('Step {}:'.format(self.steps), end='      ')
        self.print_towers()

    def move(self):
        left, mid, right = self.towers[0], self.towers[1], self.towers[2]
        while left.size != 0 or mid.size != 0:
            if mid.top is None:
                mid.push(left.pop())
            elif mid.size % 2 == 0:
                if left.top is None or left.top.data > mid.top.data:
                    left.push(mid.pop())
                else:
                    mid.push(left.pop())
            elif mid.size % 2 != 0:
                if right.top is None or right.top.data > mid.top.data:
                    right.push(mid.pop())
                else:
                    mid.push(right.pop())
            self.step()

    def print_towers(self):
        for i in range(len(self.towers)):
            print('#{}:'.format(i), end=' ')
            if self.towers[i].size == 0:
                print('<-', end='   ')
            self.towers[i].output()
        print()


if __name__ == '__main__':
    towers = TowerOfHanoi(2)
    towers.print_towers(), print()
    towers.move()
