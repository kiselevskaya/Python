# 05_sum_numbers.py

from linked_list import *


''' You have two numbers represented by a listed list, where each node contains a single digit.
    The digits are stored in reverse order, such that the 1'st digit is at the head of the list. 
    Write a function that adds the two numbers and returns the sum as a linked list.
    EXAMPLE
    Input:(7->1->6) + (5->9->2). That is, 617+295.
    Output: 2->1->9. That is, 912   
    
    Suppose the digits are stored in forward order. Repeat the above problem.
    EXAMPLE
    Input:(6->1->7) + (2->9->5). That is, 617+295.
    Output: 9->1->2. That is, 912  
'''


def sum_reverse_linked_nums(first, second):
    sum_list = LinkedList()
    remember = 0
    cur_first = first.head
    cur_second = second.head
    while cur_first is not None or cur_second is not None:
        if cur_first is None:
            sum_digits = cur_second.data+remember
        elif cur_second is None:
            sum_digits = cur_first.data+remember
        else:
            sum_digits = cur_first.data+cur_second.data+remember
        remember = sum_digits//10
        sum_list.append(Node(sum_digits % 10))

        try:
            cur_first = cur_first.next
        except Exception as e:
            pass
        try:
            cur_second = cur_second.next
        except Exception as e:
            pass
    if remember != 0:
        sum_list.append(Node(remember))

    return sum_list


def sum_linked_nums(first, second):
    first_num = ''
    seconed_num = ''
    sum_list = LinkedList()
    cur_first = first.head
    cur_second = second.head
    while cur_first is not None or cur_second is not None:
        if cur_first is None:
            seconed_num += str(cur_second.data)
        elif cur_second is None:
            first_num += str(cur_first.data)
        else:
            seconed_num += str(cur_second.data)
            first_num += str(cur_first.data)

        try:
            cur_first = cur_first.next
        except Exception as e:
            pass
        try:
            cur_second = cur_second.next
        except Exception as e:
            pass

    sum_nums = [int(i) for i in str(int(first_num)+int(seconed_num))]
    for n in sum_nums:
        sum_list.append(n)
    return sum_list


if __name__ == '__main__':
    # Test 1 sum_reverse_linked_nums
    first = LinkedList()
    for n in Node(7), Node(1), Node(6):
        first.append(n)
    print('{} list contain {} node(s)'.format('First',  first.length()), first.output())
    second = LinkedList()
    for n in Node(5), Node(9), Node(2):
        second.append(n)
    print('{} list contain {} node(s)'.format('Second',  second.length()), second.output())
    print('2->1->9   Expected')

    result = sum_reverse_linked_nums(first, second)
    print('{} list contain {} node(s)'.format('Output',  result.length()), result.output())
    print(70*'*')

    # Test 2 sum_reverse_linked_nums
    first = LinkedList()
    for n in Node(7), Node(1), Node(7), Node(9):
        first.append(n)
    print('{} list contain {} node(s)'.format('First',  first.length()), first.output())
    second = LinkedList()
    for n in Node(5), Node(9), Node(2):
        second.append(n)
    print('{} list contain {} node(s)'.format('Second',  second.length()), second.output())
    print('2->1->0->0->1   Expected')

    result = sum_reverse_linked_nums(first, second)
    print('{} list contain {} node(s)'.format('Output',  result.length()), result.output())
    print(70*'*')

    # Test 3 sum_linked_nums
    first = LinkedList()
    for n in Node(6), Node(1), Node(7):
        first.append(n)
    print('{} list contain {} node(s)'.format('First',  first.length()), first.output())
    second = LinkedList()
    for n in Node(2), Node(9), Node(5):
        second.append(n)
    print('{} list contain {} node(s)'.format('Second',  second.length()), second.output())
    print('9->1->2   Expected')

    result = sum_linked_nums(first, second)
    print('{} list contain {} node(s)'.format('Output',  result.length()), result.output())
    print(70*'*')
