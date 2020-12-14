# 01_remove_duplicates.py


class Node:
    def __init__(self, data=None):
        self.data = data    # stores node data
        self.next = None    # stores reference to the next node

    def has_value(self, value):  # to compare value with node data
        return True if self.data == value else False


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):     # adds new node to the end of list
        if not isinstance(data, Node):
            data = Node(data)

        if self.head is None:
            self.head = data
        else:
            self.tail.next = data

        self.tail = data

    def length(self):   # counts the number of nodes in list returns integer
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total

    def output(self):   # prints all nodes values
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def unsorted_search(self, value):   # searches for node with given value and returns list of indexes
        current = self.head
        cur_id = 0
        result = []
        while current is not None:
            if current.has_value(value):
                result.append(cur_id)
            current = current.next
            cur_id += 1
        return result

    def remove_by_id(self, node_id):    # removes node under given id
        current = self.head
        previous = None
        cur_id = 0

        while current is not None:
            if cur_id == node_id:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
            cur_id += 1

    '''
    Write code to remove duplicates from an unsorted linked list
    How would you solve this problem if a temporary buffer is not allowed
    '''
    def remove_duplicates_using_buffer(self):
        if self.head is None:
            return
        values = dict()
        previous = None
        current = self.head

        while current is not None:
            if current.data in values.keys():
                previous.next = current.next
            else:
                values[current.data] = True
                previous = current
            current = current.next

    def remove_duplicates(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next


if __name__ == '__main__':
    new_linked_list = LinkedList()
    for n in Node(15), Node(8.2), 'Berlin', Node(15):
        new_linked_list.append(n)
    print('Linked list contain %i node(s)' % new_linked_list.length())
    new_linked_list.output()

    # new_linked_list.remove_duplicates_using_buffer()
    new_linked_list.remove_duplicates()
    print('Linked list contain %i node(s)' % new_linked_list.length())
    new_linked_list.output()

