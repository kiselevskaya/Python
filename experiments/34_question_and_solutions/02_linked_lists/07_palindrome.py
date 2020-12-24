# 07_palindrome.py


from linked_list import *


def is_palindrome(linked):
    length = 0
    node = linked.head
    while node is not None:
        length += 1
        node = node.next
    palindrome = comparison(linked.head, length)
    print('\n', 'Palindrome' if palindrome is None else 'Not palindrome')
    return True if palindrome is None else False


def comparison(node, length):
    if length == 1 or length == 0:  # Reach the middle, returns next to the list middle node
        return node.next if length == 1 else node
    back = comparison(node.next, length-2)
    try:
        return back.next if node.data == back.data else False
    except Exception as e:
        return False


if __name__ == '__main__':
    # Test 1
    print(70*'*', '\n', 'Test 1')
    linked = LinkedList()
    for n in list('73537'):
        linked.append(Node(n))
    linked.output()
    assert is_palindrome(linked) is True, '7->3->5->3->7 is a palindrome'

    # Test 2
    print(70*'*', '\n', 'Test 2')
    linked2 = LinkedList()
    for n in list('735537'):
        linked2.append(Node(n))
    linked2.output()
    assert is_palindrome(linked2) is True, '7->3->5->5->3->7 is a palindrome'

    # Test 3
    print(70*'*', '\n', 'Test 3')
    linked3 = LinkedList()
    for n in list('735337'):
        linked3.append(Node(n))
    linked3.output()
    assert is_palindrome(linked3) is False, '7->3->5->3->3->7 is NOT a palindrome'

    # Test 4
    print(70*'*', '\n', 'Test 4')
    linked4 = LinkedList()
    for n in list('madam'):
        linked4.append(Node(n))
    linked4.output()
    assert is_palindrome(linked4) is True, 'm->a->d->a->m is a palindrome'

    # Test 5
    print(70*'*', '\n', 'Test 5')
    linked5 = LinkedList()
    for n in list('madman'):
        linked5.append(Node(n))
    linked5.output()
    assert is_palindrome(linked5) is False, 'm->a->d->m->a->n is a NOT palindrome'
