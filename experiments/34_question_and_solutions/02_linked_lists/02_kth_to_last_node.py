# 02_kth_to_last_node.py


class Node:
    def __init__(self, data=None):
        self.data = data    # stores node data
        self.next = None    # stores reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):   # counts the number of nodes in list returns integer
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total

    def append(self, data):     # adds new node to the end of list
        if not isinstance(data, Node):
            data = Node(data)
        if self.head is None:
            self.head = data
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = data

    def output(self):   # prints all nodes values
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


'''Implement an algorithm to find the kth to last element of singly linked list.'''


def kth_to_last_node(linked, k):
    index = 0
    current = linked.head
    output = []
    while current is not None:
        if k == index:
            runner = current
            while runner is not None:
                output.append(runner.data)
                runner = runner.next
            return output
        else:
            current = current.next
            index += 1


if __name__ == '__main__':
    linked = LinkedList()
    for n in Node(15), Node(8.2), 'Berlin', Node(15):
        linked.append(n)
    print('Linked list contain %i node(s)' % linked.length())
    linked.output()

    print(kth_to_last_node(linked, 0))      # '15', '8.2', 'Berlin', '15'
    print(kth_to_last_node(linked, 1))      # '8.2', 'Berlin', '15'
    print(kth_to_last_node(linked, 2))      # 'Berlin', '15'
    print(kth_to_last_node(linked, 3))      # '15'
    print(kth_to_last_node(linked, 4))      # None
    print(kth_to_last_node(linked, -1))     # None
