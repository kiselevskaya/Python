# list_as_stacks.py

def push(stack_num, value):  # Stack number 0, 1 or 2
    # Check if there are space
    if stack_pointer[stack_num]+1 >= stack_size:    # last element
        print('Out of space')
        return
    stack_pointer[stack_num] += 1     # increment pointer
    buffer[top_of_stack(stack_num)] = value     # update value


def pop(stack_num):
    if stack_pointer[stack_num] == -1:      # check if stack is empty
        print('Trying to pop an empty stack')
        return
    value = buffer[top_of_stack(stack_num)]     # remember value of top item
    buffer[top_of_stack(stack_num)] = None      # remove the top item
    stack_pointer[stack_num] -= 1       # decrement pointer after popping an item
    return value


def peek(stack_num):
    return buffer[top_of_stack(stack_num)]      # return the top item of a stack


def top_of_stack(stack_num):        # returns absolut index of stack <stack_num>
    return stack_size*stack_num+stack_pointer[stack_num]


if __name__ == '__main__':
    stack_size = 3
    buffer = [None]*(stack_size * 3)    # List <buffer> as <3> stacks
    stack_pointer = [-1, -1, -1]    # to track top element

    # test
    peeks = []
    values = [['Norway', 'Canada', 'Iceland', 'USA'],
              ['is constructing', '42', 'does not have', 'have'],
              ['airport', 'a railway system', 'harbour', 'bridge']]
    for stack in range(3):
        for value in values[stack]:
            push(stack, value)
    print(buffer)
    print('-'*120)
    for i in range(3):
        peeks.append(peek(i))
    print(*peeks)
    pop(2)
    peeks.pop()
    peeks.append(peek(2))
    print(*peeks)


