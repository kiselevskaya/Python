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
    rest = 0
    cur_first = first.head
    cur_second = second.head
    while cur_first is not None or cur_second is not None:
        if cur_first is None:
            sum_digits = cur_second.data+rest
        elif cur_second is None:
            sum_digits = cur_first.data+rest
        else:
            sum_digits = cur_first.data+cur_second.data+rest
        rest = sum_digits//10
        sum_list.append(Node(sum_digits % 10))

        try:
            cur_first = cur_first.next
        except Exception as e:
            pass
        try:
            cur_second = cur_second.next
        except Exception as e:
            pass
    if rest != 0:
        sum_list.append(Node(rest))

    return sum_list

########################################################################################################################
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


########################################################################################################################
def sum_reversed_lists_recursively(node1, node2, rest=0, output=LinkedList()):
    if node1 is None and node2 is None and rest == 0:
        return

    value = rest
    if node1 is None and node2 is None:
        pass
    elif node1 is None:
        value += node2.data
    elif node2 is None:
        value += node1.data
    else:
        value += node1.data + node2.data

    output.append(Node(value % 10))

    if node1 is not None or node2 is not None or value >= 10:
        sum_reversed_lists_recursively((node1.next if node1 is not None else None),
                                       (node2.next if node2 is not None else None),
                                       int(1 if value >= 10 else 0), output)
    return output


########################################################################################################################
def prepare_lists(first, second):
    if first.head is None and second.head is None:
        return
    diff = first.length() - second.length()
    if diff < 0:
        make_length_equal(first, abs(diff))
    elif diff > 0:
        make_length_equal(second, diff)
    output = LinkedList()
    return output


def make_length_equal(linked, diff):
    for i in range(diff):
        insert_before(Node(0), linked)
    return linked


def insert_before(node, linked):
    node.next = linked.head
    linked.head = node
    return linked


########################################################################################################################
if __name__ == '__main__':
    print(70*'*', '\n', 'Set 1')
    first = LinkedList()
    for n in Node(7), Node(1), Node(6):
        first.append(n)
    first.output(), print('First number')
    second = LinkedList()
    for n in Node(5), Node(9), Node(2):
        second.append(n)
    second.output(), print('Second number')

    print(70*'*', '\n', 'Set 2')
    first2 = LinkedList()
    for n in Node(7), Node(1), Node(7), 9:
        first2.append(n)
    first2.output(), print('First number')
    second2 = LinkedList()
    for n in Node(5), Node(9), Node(2):
        second2.append(n)
    second2.output(), print('   Second number')

    print(70*'*', '\n', 'Set 3')
    first3 = LinkedList()
    for n in Node(6), Node(1), Node(7):
        first3.append(n)
    first3.output(), print('First number')
    second3 = LinkedList()
    for n in Node(2), Node(9), Node(5):
        second3.append(n)
    second3.output(), print('Second number')

    print(70*'*', '\n', 'Set 4')
    first4 = LinkedList()
    for n in Node(6), Node(1), Node(7), 0:
        first4.append(n)
    first4.output(), print('First number')
    second4 = LinkedList()
    for n in Node(2), Node(9), Node(5):
        second4.append(n)
    second4.output(), print('   Second number')

    ########################################################################################
    # Test 1 sum_reverse_linked_nums
    print(70*'*', '\n', 'Test 1')
    print('2->1->9   Expected result of Set 1')
    result = sum_reverse_linked_nums(first, second)
    result.output(), print('Result')

    # Test 2 sum_reverse_linked_nums
    print(70*'*', '\n', 'Test 2')
    print('2->1->0->0->1   Expected result of Set 2')
    result = sum_reverse_linked_nums(first2, second2)
    result.output(), print('Result')

    # Test 3 sum_linked_nums
    print(70*'*', '\n', 'Test 2')
    print('9->1->2   Expected result of Set 3')
    result = sum_linked_nums(first3, second3)
    result.output(), print('Result')

    # Test 4 sum_reversed_lists_recursively
    print(70*'*', '\n', 'Test 4')
    print('2->1->9   Expected result of Set 1')
    result = sum_reversed_lists_recursively(first.head, second.head, 0, LinkedList())
    result.output(), print('Result')

    # Test 5 sum_reversed_lists_recursively
    print(70*'*', '\n', 'Test 5')
    print('2->1->0->0->1   Expected result of Set 2')
    result = sum_reversed_lists_recursively(first2.head, second2.head, 0, LinkedList())
    result.output(), print('Result')

    # Test 6
    print(70*'*', '\n', 'Test 6')
    print('6->4->6->5   Expected result of Set 4')
    prepare_lists(first4, second4)
    first4.output(), print()
    second4.output()



