# 03_delete_node.py


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        total = 0
        current = self.head
        while current is not None:
            current = current.next
            total += 1
        return total

    def append(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        if self.head is None:
            self.head = data
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = data

    def output(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete_node_by_data(self, data):
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
            previous = current
            current = current.next

    def return_node_by_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next

    '''Implement an algorithm to delete a node in the middle of singly linked list, given only access to that node'''
    def delete_node(self, node=None):
        try:
            node.data = node.next.data
            node.next = node.next.next
        except Exception as e:
            print(e)


if __name__ == '__main__':
    linked = LinkedList()
    for n in Node(15), Node(8.2), 'Berlin', Node('15'):
        linked.append(n)
    print('Linked list contain %i node(s)' % linked.length())
    linked.output()

    # linked.delete_node(15)
    # print('Linked list contain %i node(s)' % linked.length())
    # linked.output()

    node = linked.return_node_by_data('Berlin')
    linked.delete_node(node)
    print('Linked list contain %i node(s)' % linked.length())
    linked.output()
