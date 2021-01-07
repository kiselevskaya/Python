# list_as_stacks_flexible.py


class StackData:

    def __init__(self, _start, _capacity):
        self.start = _start
        self.pointer = self.start-1
        self.size = 0
        self.capacity = _capacity

    def is_within_stack(self, index, total_size):
        if self.start < index <= self.start+self.capacity:      # non-wrapping
            return True
        if self.start > index <= (self.start+self.capacity) % total_size:       # wrapping
            return True
        return False


class MultiStack:

    def __init__(self, stacks_number=3, stack_size=4):
        self.number_of_stacks = stacks_number
        self.default_size = stack_size
        self.total_size = self.number_of_stacks * self.default_size
        self.stacks = [StackData(0, self.default_size),
                       StackData(self.default_size, self.default_size),
                       StackData(self.default_size * 2, self.default_size)]
        self.buffer = [None]*self.total_size

    def number_of_elements(self):
        return self.stacks[0].size + self.stacks[1].size + self.stacks[2].size

    def next_element(self, index):       # returns an an index of the next element
        return 0 if index + 1 == self.total_size else index+1

    def previous_element(self, index):       # returns an an index of the previous element
        return self.total_size-1 if index == 0 else index-1

    def shift(self, stack_num):
        stack = self.stacks[stack_num]
        if stack.size >= stack.capacity:
            next_stack = (stack_num+1) % self.number_of_stacks
            self.shift(next_stack)      # make room for another stack
            stack.capacity += 1

        # go through the stack starting from the last element
        i = (stack.start+stack.capacity-1) % self.total_size
        while stack.is_within_stack(i, self.total_size):
            self.buffer[i] = self.buffer[self.previous_element(i)]
            i = self.previous_element(i)

        self.buffer[stack.start] = None     # update the shifted stack main data
        stack.start = self.next_element(stack.start)
        stack.pointer = self.next_element(stack.pointer)
        stack.capacity -= 1     # set the default capacity

    def expand(self, stack_num):        # Expand stack by shifting over other stacks
        self.shift((stack_num+1) % self.number_of_stacks)
        self.stacks[stack_num].capacity += 1

    def push(self, stack_num, value):
        stack = self.stacks[stack_num]
        if stack.size >= stack.capacity:        # Check for space within stack
            if self.number_of_elements() >= self.total_size:        # Check for space in total
                print('Out of space')
                return
            else:       # Make some room in stack
                self.expand(stack_num)

        stack.size += 1
        stack.pointer = self.next_element(stack.pointer)
        self.buffer[stack.pointer] = value

    def pop(self, stack_num):
        stack = self.stacks[stack_num]
        if stack.size == 0:
            print('Trying to pop an empty stack')
            return
        value = self.buffer[stack.pointer]
        self.buffer[stack.pointer] = None
        stack.pointer = self.previous_element(stack.pointer)
        stack.size -= 1
        return value

    def peek(self, stack_num):
        stack = self.stacks[stack_num]
        return self.buffer[stack.pointer]

    def is_empty(self, stack_num):
        return self.stacks[stack_num].size == 0


if __name__ == '__main__':
    # Test 1 (push)
    multi_stack = MultiStack()
    multi_stack.push(0, 'F')
    multi_stack.push(1, 'e')
    multi_stack.push(2, 'b')
    multi_stack.push(0, 'r')
    multi_stack.push(1, 'a')
    multi_stack.push(2, 'u')
    multi_stack.push(0, 'o')
    multi_stack.push(1, 't')
    multi_stack.push(2, 'g')
    multi_stack.push(0, 'g')
    multi_stack.push(2, 's')
    print(multi_stack.buffer)

    # Test 2 (shift)
    multi_stack.push(0, 's')
    print(multi_stack.buffer)

    # Test 3 (shift) Failed
    multi_stack.pop(0)
    print(multi_stack.buffer)
    multi_stack.pop(2)

    multi_stack.pop(1)
    multi_stack.pop(1)
    multi_stack.pop(1)
    multi_stack.push(2, 's')

    multi_stack.push(1, 'h')
    multi_stack.push(1, 'a')
    multi_stack.push(1, 't')
    print(multi_stack.buffer)
    multi_stack.push(1, 'e')
    print(multi_stack.buffer)
