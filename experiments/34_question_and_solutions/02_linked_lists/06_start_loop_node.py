# 06_start_loop_node.py


from linked_list import *


def start_loop_node(head):
    slow = head     # runs with k=1 speed
    fast = head     # runs with 2k speed
    # Collision point of SlowRunner and FastRunner is loop_size-k (mod(k, loop_size)) into the linked list
    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
        if fast.data == slow.data:  # Collision
            break
    # check for no loop
    if fast is None or fast.next is None:
        return
    # SlowRunner moves to head so now SlowRunner and FastRunner are k steps away from start loop
    # If move SlowRunner and FastRunner at the same speed they collide at the start loop
    slow = head
    while slow.data != fast.data:
        slow = slow.next
        fast = fast.next
    return fast


if __name__ == '__main__':
    # Test 1
    circular = LinkedList()
    for n in 'A', 'B', 'C', 'D', 'E', 'C':
        circular.append(Node(n))
    node = circular.head
    loop = None
    while node.next is not None:
        if node.data == 'D':
            loop = node
        node = node.next
    node.next = loop

    # Test 2
    circular2 = LinkedList()
    for n in 'A', 'B', 'C', 'D', 'E', 'B':
        circular2.append(Node(n))
    node2 = circular2.head
    loop2 = None
    while node2.next is not None:
        if node2.data == 'C':
            loop2 = node2
        node2 = node2.next
    node2.next = loop2

    # Test 1
    circular3 = LinkedList()
    for n in 'A', 'B', 'C', 'D', 'E', 'A':
        circular3.append(Node(n))
    node3 = circular3.head
    loop3 = None
    while node3.next is not None:
        if node3.data == 'B':
            loop3 = node3
        node3 = node3.next
    node3.next = loop3

    start_loop = start_loop_node(circular.head)
    print(start_loop.data)
    assert (start_loop.data == 'C'), 'Failed, the start loop is C'

    start_loop2 = start_loop_node(circular2.head)
    print(start_loop2.data)
    assert (start_loop2.data == 'B'), 'Failed, the start loop is B'

    start_loop3 = start_loop_node(circular3.head)
    print(start_loop3.data)
    assert (start_loop3.data == 'A'), 'Failed, the start loop is A'
