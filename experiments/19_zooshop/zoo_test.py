
'''
def add_animal(fname):
    print()
    species = str(input('Enter species: '))
    name = str(input('Enter Name of animal: '))
    age = str(input('Enter age in format <number> year(s)/month(s): '))
    with open(fname, 'a+') as f:
        f.write(' '.join((species, name, age)) + '\n')
    f.close()


def animal_sold(fname):
    animals = [arr[0].split(' ') for arr in [l.split('\n') for l in open(fname, 'rt')]]
    new_list = '../00_text_files/animals.txt'
    sold = str(input('Enter name of sold animal: '))
    for arr in animals:
        if sold in arr:
            animals.pop(animals.index(arr))
    with open(new_list, 'wt') as f:
        for x in animals:
            f.write(' '.join((x[0], x[1], x[2], x[3])) + '\n')
        f.close()


def print_animals_list(fname):
    print('{}{}{}{}'.format('Species'.ljust(12), 'Name'.ljust(12),
          'Age'.ljust(12), 'Description'.ljust(12)))
    print()
    animals = [arr[0].split(' ') for arr in [l.split('\n') for l in open(fname, 'rt')]]
    for arr in animals:
        print('{}{}{}'.format(arr[0].ljust(12), arr[1].ljust(12), ' '.join((arr[2], arr[3])).ljust(12)))
'''


import random


class Animal:
    def __init__(self, name=None, age=None, weight=None, lifespan=None, obesity=None, species=None,
                 description=None, massif=None, names_list = '../00_text_files/names_list.txt'):
        self.name = name
        self.age = age
        self.weight = weight
        self.lifespan = lifespan
        self.obesity = obesity
        self.species = species
        self.description = description
        self.massif = massif
        self.names_list = names_list

    def __repr__(self):
       return ('{}{}{}{}{}'.format(self.name.ljust(12), str(self.age).center(12),
                str(self.weight).center(12), str(self.description).ljust(23), str(self.species).ljust(12)))

    def get_name(self):
        arr = []
        for name in [l.split('\n') for l in open(self.names_list, 'rt')]:
            arr.append(name[0])
        name = random.choice(arr)
        return name

    def aging(self):
        self.age += 0.08
        return self.age

    def death(self):
        for animal in self.massif:
            if self.age >= self.lifespan or self.weight >= self.obesity:
                self.massif.pop(self.massif.index(animal))


class Wolf(Animal):
    def __init__(self, name=None, age=None, weight=None, lifespan=None, obesity=None, description=None, species=None):
        Animal.__init__(self, name, age, weight, lifespan, obesity, description, species, massif=None)
        if self.name is None:
            self.name = self.get_name()
        if self.age is None:
            self.age = random.randint(0, 4)
        if self.weight is None:
            self.weight = round(random.uniform(4.0, 20.0), 2)
        if self.description is None:
            self.description = 'vegetarian'
        if self.species is None:
            self.species = 'wolf'
        if self.obesity is None:
            self.obesity = 80
        if self.lifespan is None:
            self.lifespan = 10

if __name__ == '__main__':
    animals = []
    val = Wolf()
    animals.append(val)
    print(animals)

