# -*- coding: utf-8 -*-

import random
import time
import math


month = 0.083  #1/12


class Names:
    def __init__(self, female='../00_text_files/female_names.txt', male='../00_text_files/male_names.txt'):
        self.female = female
        self.male = male

    def get_female(self):
        arr = []
        for name in [l.split('\n') for l in open(self.female, 'rt')]:
            arr.append(name[0])
        name = random.choice(arr)
        return name

    def get_male(self):
        arr = []
        for name in [l.split('\n') for l in open(self.male, 'rt')]:
            arr.append(name[0])
        name = random.choice(arr)
        return name


class Animal(Names):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        global month
        self.gender = gender
        self.name = name
        self.age = age
        self.weight = weight
        self.lifespan = lifespan
        self.obesity = obesity
        self.species = species
        self.description = description

    def get_gender(self, sex):
        if self.get_gender is None and sex is None:
            self.gender = random.choice(['female', 'male'])
        else:
            self.gender = sex
        return self.gender

    def get_name(self, sex, nick):
        if self.name is None and nick is None and self.get_gender(sex) == 'female':
            self.name = self.get_female()
        elif self.name is None and nick is None and self.get_gender(sex) == 'male':
            self.name = self.get_male()
        else:
            self.name = nick
        return self.name

    def get_age(self, max_age, years):
        if self.age is None and years is None:
            self.age = round(random.uniform(month, max_age), 2)
        else:
            self.age = years
        return self.age

    def get_weight(self, min_weight, max_weight, tons):
        if self.weight is None and tons is None:
            self.weight = round(random.uniform(min_weight, max_weight), 2)
        else:
            self.weight = tons
        return self.weight

    def __repr__(self):
        return ('{}{}{}{}{}{}'.format(str(self.gender).ljust(12), str(self.name).ljust(12), str(self.age).center(12),
                 str(self.weight).center(12), str(self.description).ljust(23), str(self.species).ljust(12)))

    def aging(self):
        self.age += 3.083
        return self.age

    def growth(self):
        self.weight += round(random.uniform(0.2, 0.5), 2)
        return self.weight

    def old_age(self):
        if self.age >= self.lifespan:
            print('\n', ('{} {} DIED OF OLD AGE'.format(self.species, self.name)).center(83))
            return True

    def fat(self):
        if self.weight >= self.obesity:
            print('\n', ('{} {} DIED OF OBESITY'.format(self.species, self.name)).center(83))
            return True


class Wolf(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None, lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = self.get_gender(gender)
        self.name = self.get_name(gender, name)
        self.age = self.get_age(16, age)
        self.weight = self.get_weight(0.5, 12, weight)
        if self.description is None:
            self.description = 'vegetarian'
        if self.species is None:
            self.species = 'wolf'
        if self.obesity is None:
            self.obesity = 80
        if self.lifespan is None:
            self.lifespan = 75

'''
class Parrot(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None, lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = self.get_gender
        self.name = name
        self.age = self.get_age
        if self.weight is None:
            self.weight = round(random.uniform(0.3, 2.0), 2)
        if self.description is None:
            self.description = 'bites visitors'
        if self.species is None:
            self.species = 'parrot'
        if self.obesity is None:
            self.obesity = 10
        if self.lifespan is None:
            self.lifespan = 65


class Raven(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None, lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = gender
        self.name = name
        self.age = self.get_age
        if self.weight is None:
            self.weight = round(random.uniform(0.3, 2.0), 2)
        if self.description is None:
            self.description = 'doubts its existence'
        if self.species is None:
            self.species = 'raven'
        if self.obesity is None:
            self.obesity = 9
        if self.lifespan is None:
            self.lifespan = 65


class Lizard(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None, lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = gender
        self.name = name
        self.age = self.get_age
        if self.weight is None:
            self.weight = round(random.uniform(0.02, 1.5), 2)
        if self.description is None:
            self.description = 'secretive'
        if self.species is None:
            self.species = 'lizard'
        if self.obesity is None:
            self.obesity = 15
        if self.lifespan is None:
            self.lifespan = 50


class New(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None, lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = gender
        self.name = name
        if self.age is None:
            self.age = 0
        if self.weight is None:
            self.weight = round(random.uniform(0.07, 0.19), 2)
        if self.description is None:
            self.description = 'sluggish'
        if self.species is None:
            self.species = 'lizard'
        if self.obesity is None:
            self.obesity = 12
        if self.lifespan is None:
            self.lifespan = 50
'''


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

    def options(self):
        x = None
        while x != 0 or x != 1:
            print()
            x = int(input('Enter 0 to see all animals or 1 to add one more: '))
            print()
            if x == 0:
                self.get_list()
            elif x == 1:
                self.add_animal()

    def incident(self):
        if len(self.array) >= 2:
            hungry = random.choice(self.array)
            food = random.choice(self.array)
            if hungry.weight != food.weight and hungry.weight >= (food.weight*2):
                print('\n ', ('{} {} SWALLOWED UP {} {}'.format(hungry.species, hungry.name, food.species, food.name)).center(71))
                hungry.weight += food.weight
                self.array.pop(self.array.index(food))

    def reproduction(self):
        x = random.choice(self.array)
        y = random.choice(self.array)
        if x != y and x.gender != y.gender and abs(x.weight-y.weight) <= min(x.weight, y.weight):
            num_child = random.randint(1, 4)
            print()
            print('\n', ('{} NEWBORNS!'.format(num_child)).center(71))
            num = 0
            while num != num_child:
                num += 1
                life = sum([x.lifespan, y.lifespan]) // 2
                obes = sum([x.obesity, y.obesity]) // 2
                descr = random.choice([x.description, y.description])
                if x.species == y.species:
                    spec = x.species
                else:
                    spec = '{}-{}'.format(x.species, y.species)
                new = New(lifespan=life, obesity=obes, description=descr, species=spec)
                self.array.append(new)


if __name__ == '__main__':
    animals = []
    wolf = Wolf('male', weight=10)
#    lizard = Lizard()
#    raven = Raven()
#    gonzo = Lizard()
#    parrot = Parrot()
    animals.append(wolf)
    #animals.append(den)  #lizard, raven, gonzo, parrot))
    zoo = Shop(animals)
    zoo.get_list()

'''
    def time_later(beasts, shop):
        print('\n', 'Years later'.center(71))
        for beast in beasts:
            beast.aging()
            beast.growth()
            if beast.old_age() or beast.fat():
                beasts.pop(beasts.index(beast))
        shop.incident()
        shop.reproduction()
        time.sleep(2)

    while True:
        time_later(animals, zoo)
        zoo.get_list()
'''
