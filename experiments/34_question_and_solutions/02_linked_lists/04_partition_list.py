# 04_partition_list.py


from linked_list import *


def partition_list(linked, x):
    ''' Starts with second element as it doesn't meter if first is smaller or bigger than X, it will be the border element.
        Elements smaller than X will be moved to the head of the list.
        So all elements to the left included (or excluded if first element wasn't less than x) the border element are less than X.
        All elements to the right included (or excluded if first element was less than x) the border element are bigger or equal to X.
    '''
    current = linked.head.next
    previous = linked.head
    while current is not None:
        if current.data < x:
            previous.next = current.next
            current.next = linked.head
            linked.head = current
            current = previous.next
        else:
            previous = current
            current = current.next


if __name__ == '__main__':
    linked = LinkedList()
    for n in Node(-1), Node(15), Node(-3), 8.2, Node(14), Node(-8):
        linked.append(n)
    print('Linked list contain %i node(s)' % linked.length())
    linked.output()
    print('--------')

    partition_list(linked, 0)
    print('Linked list contain %i node(s)' % linked.length())
    linked.output()
