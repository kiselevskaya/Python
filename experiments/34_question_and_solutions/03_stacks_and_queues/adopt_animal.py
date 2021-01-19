# adopt_animal.py


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        self.size += 1
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is not None:
            self.size -= 1
            value = self.top.data
            self.top = self.top.next
            return value
        print('Trying to pop an empty list')
        return

    def peek(self):
        try:
            return self.top.data
        except Exception as e:
            pass

    def is_empty(self):
        return self.top is None

    def output(self):
        if self.is_empty():
            print('-empty-', end='  ')
        current = self.top
        while current is not None:
            if current.next is None:
                print(current.data, end='  ')
            else:
                print(current.data, end=' <- ')
            current = current.next


class Shelter:
    def __init__(self):
        self.shelter = LinkedList()
        self.room = LinkedList()
        self.buffer = LinkedList()

    def shift(self):    # shift animals from shelter to the room that oldest will live it first
        if self.room.is_empty():
            while not self.shelter.is_empty():
                self.room.push(self.shelter.pop())

    def empty_buffer(self):     # return animals to the room
        while not self.buffer.is_empty():
            self.room.push(self.buffer.pop())

    def check_room(self, species):        # find cat or dog in room
        while not self.room.is_empty():
            if self.room.peek().find(species) > -1:
                return self.room.pop()
            else:
                self.buffer.push(self.room.pop())
        return

    def check_shelter(self, species):
        dog = self.check_room(species)
        if not dog:     # if no found in room check in entire shelter
            self.shift()
            dog = self.check_room(species)
        self.empty_buffer()
        return dog

    def enqueue(self, animal):
        self.shelter.push(animal)

    def dequeue_any(self):
        self.shift()
        return self.room.pop()

    def dequeue_dog(self):
        self.shift()
        return self.check_shelter('dog')

    def dequeue_cat(self):
        self.shift()
        return self.check_shelter('cat')

    def show_animals(self):
        print('Shelter stack:', end=' '), self.shelter.output()
        print('Adopt room stack:', end=' '), self.room.output()
        print('Buffer stack:', end=' '), self.buffer.output()
        print()


if __name__ == '__main__':
    shelter = Shelter()

    animals = ['cat_0', 'cat_1', 'cat_2', 'dog_3']
    for animal in animals:
        shelter.enqueue(animal)
    shelter.show_animals()

    print('\n', shelter.dequeue_any(), 'ready to leave')
    shelter.show_animals()

    print('\n', shelter.dequeue_dog(), 'ready to leave')
    shelter.show_animals()

    for animal in ['dog_4', 'dog_5', 'dog_6', 'cat_7', 'dog_8', 'dog_9', 'cat_10', 'cat_11', 'dog_12', 'cat_13', 'cat_14']:
        shelter.enqueue(animal)
    shelter.show_animals()

    print('\n', shelter.dequeue_dog(), 'ready to leave')
    shelter.show_animals()

    print('\n', shelter.dequeue_cat(), 'ready to leave')
    shelter.show_animals()

    print('\n', shelter.dequeue_cat(), 'ready to leave')
    shelter.show_animals()

    print('\n', shelter.dequeue_cat(), 'ready to leave')
    shelter.show_animals()

