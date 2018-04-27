# -*- coding: utf-8 -*-

import random
import time

month = 0.083  # 1 / 12


class Names:
    def __init__(self, female='../00_text_files/female_names.txt',
                 male='../00_text_files/male_names.txt'):
        self.female = female
        self.male = male
        self.female_list = None
        self.male_list = None

    def create_female_name(self):
        if self.female_list is None:
            self.female_list = []
            for name in [l.split('\n') for l in open(self.female, 'rt')]:
                self.female_list.append(name[0])
        return random.choice(self.female_list)

    def create_male_name(self):
        arr = []
        for name in [l.split('\n') for l in open(self.male, 'rt')]:
            arr.append(name[0])
        return random.choice(arr)

    def create_name(self, gender):
        if gender == 'female':
            return self.create_female_name()
        elif gender == 'male':
            return self.create_male_name()


class Animal(Names):
    def __init__(self, gender, name, age=None, max_age=None, weight=None, min_weight=None,
                 max_weight=None, lifespan=None, life_limit=None, obesity=None, fat_limit=None,
                 description=None, feature=None, species=None, kind=None):
        super().__init__()
        global month
        self.gender = random.choice(['female', 'male']) if gender is None else gender
        self.name = self.create_name(self.gender) if name is None else name
        self.age = round(random.uniform(month, max_age), 2) if age is None else age
        self.weight = round(random.uniform(min_weight, max_weight), 2) if weight is None else weight
        self.lifespan = life_limit if lifespan is None else lifespan
        self.obesity = fat_limit if obesity is None else obesity
        self.species = kind if species is None else species
        self.description = feature if description is None else description

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_description(self):
        return self.description

    def get_species(self):
        return self.species

    def get_obesity(self):
        return self.obesity

    def get_lifespan(self):
        return self.lifespan

    def __repr__(self):
        return ('{}{}{}{}{}{}'.format(str(self.gender).ljust(12), str(self.name).ljust(12),
                                      str(round(self.age, 2)).ljust(12), str(round(self.weight, 2)).ljust(12),
                                      str(self.description).ljust(23), str(self.species).ljust(12)))

    def aging(self):
        self.age += 3.083
        return self.age

    def growth(self):
        self.weight += round(random.uniform(0.2, 0.5), 2)
        return self.weight

    def old_age(self):
        if self.age >= self.lifespan:
            print('\n', ('{} {} ☠ DIED OF OLD AGE ☠'.format(self.species, self.name)).center(83))
            return True

    def too_fat(self):
        if self.weight >= self.obesity:
            print('\n', ('{} {} ☠ DIED OF OBESITY ☠'.format(self.species, self.name)).center(83))
            return True


class Wolf(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__(gender, name, age, 16, weight, 0.5, 8, lifespan, 75,
                         obesity, 80, description, 'vegetarian', species, 'wolf')


class Parrot(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__(gender, name, age, 13, weight, 0.3, 2, lifespan, 65,
                         obesity, 10, description, 'bites visitors', species, 'parrot')


class Raven(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__(gender, name, age, 15, weight, 0.3, 2, lifespan, 65,
                         obesity, 9, description, 'doubts its existence', species, 'raven')


class Lizard(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__(gender, name, age, 18, weight, 0.1, 3, lifespan, 50,
                         obesity, 15, description, 'sluggish', species, 'lizard')


class New(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__(gender, name, age, 7, weight, 0.07, 0.19, lifespan, 50,
                         obesity, 12, description, 'secretive', species, 'indefinite')


class Shop:
    def __init__(self, array):
        self.array = array
        self.title = ('{}{}{}{}{}{}'.format('Gender'.ljust(12), 'Name'.ljust(12), 'Age(years)'.ljust(12),
                      'Weight(kg)'.ljust(12), 'Description'.ljust(23), 'Species'.ljust(12)))

    def get_list(self):
        print('\n', self.title, '\n')
        for i in self.array:
            print(i)

    def add_animal(self):
        gender = str(input('Enter gender: '))
        name = str(input('Enter animal name: '))
        age = int(input('Enter age in years: '))
        weight = float(input('Enter animal weight: '))
        lifespan = int(input('Enter lifespan in years: '))
        obesity = int(input('Enter obesity in kg: '))
        description = str(input('Enter description: '))
        species = str(input('Enter species: '))
        new = New(gender, name, age, weight, lifespan, obesity, description, species)
        self.array.append(new)

    def get_animals(self):
        return self.array

    def options(self):
        x = None
        while x != 0 or x != 1:
            x = int(input('\n Enter 0 to see all animals or 1 to add one more: '))
            if x == 0:
                self.get_list()
            elif x == 1:
                self.add_animal()

    def incident(self):
        if len(self.array) >= 2:
            hungry = random.choice(self.array)
            food = random.choice(self.array)
            if hungry != food and hungry.weight >= (food.weight*2):
                print('\n ', ('{} {} ♻ SWALLOWED UP ♻ {} {}'.format(hungry.species, hungry.name,
                                                                food.species, food.name)).center(83))
                hungry.weight += food.weight
                self.array.pop(self.array.index(food))

    def reproduction(self):
        x = random.choice(self.array)
        y = random.choice(self.array)
        if x != y and x.gender != y.gender and abs(x.weight-y.weight) <= min(x.weight, y.weight):
            strength = random.randint(1, 4)
            print('\n', ('{} ✷※ NEWBORNS! ※✷'.format(strength)).center(83))
            num = 0
            while num != strength:
                num += 1
                max_age = sum([x.lifespan, y.lifespan]) // 2
                fatness = sum([x.obesity, y.obesity]) // 2
                feature = random.choice([x.description, y.description])
                if x.species == y.species:
                    kind = x.species
                else:
                    kind = '{}-{}'.format(x.species, y.species)
                new = New(age=0, lifespan=max_age, obesity=fatness, description=feature, species=kind)
                self.array.append(new)


def time_later(zoo):
    print('\n', 'Some time later'.center(71))
    animals = zoo.get_animals()
    for animal in animals:
        animal.aging()
        animal.growth()
        if animal.old_age() or animal.too_fat():
            animals.pop(animals.index(animal))
    zoo.incident()
    zoo.reproduction()
    time.sleep(2)


def simulate(zoo):
    while True:
        time_later(zoo)
        zoo.get_list()


def main():
    animals = []
    wolf = Wolf('male', weight=6)
    lizard = Lizard()
    raven = Raven()
    gonzo = Lizard()
    parrot = Parrot()
    animals.append(wolf)
    animals.extend([lizard, raven, gonzo, parrot])
    zoo = Shop(animals)
    zoo.get_list()

    simulate(zoo)


if __name__ == '__main__':
    main()
