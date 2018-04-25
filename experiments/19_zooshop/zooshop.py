# -*- coding: utf-8 -*-

import random
import time
import math


month = 0.083  #1/12


class Names:
    def __init__(self, female='../00_text_files/female_names.txt',
                 male='../00_text_files/male_names.txt'):
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
        if self.gender is None:
            if sex is None:
                self.gender = random.choice(['female', 'male'])
            else:
                self.gender = sex
        return self.gender

    def get_name(self, sex, nick):
        if self.name is None:
            if nick is None:
                if sex == 'female':
                    self.name = self.get_female()
                elif sex == 'male':
                    self.name = self.get_male()
            else:
                self.name = nick
        return self.name

    def get_age(self, years, max_age):
        if self.age is None:
            if years is None:
                self.age = round(random.uniform(month, max_age), 2)
            else:
                self.age = years
        return self.age

    def get_weight(self, tons, min_weight, max_weight):
        if self.weight is None:
            if tons is None:
                self.weight = round(random.uniform(min_weight, max_weight), 2)
            else:
                self.weight = tons
        return self.weight

    def get_description(self, definition, feature):
        if self.description is None:
            if definition is None:
                self.description = feature
            else:
                self.description = definition
        return self.description

    def get_species(self, sort, kind):
        if self.species is None:
            if sort is None:
                self.species = kind
            else:
                self.species = sort
        return self.species

    def get_obesity(self, fatness, fat):
        if self.obesity is None:
            if fatness is None:
                self.obesity = fat
            else:
                self.obesity = fatness
        return self.obesity

    def get_lifespan(self, ages, limit):
        if self.lifespan is None:
            if ages is None:
                self.lifespan = limit
            else:
                self.lifespan = ages
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
            print('\n', ('{} {} DIED OF OLD AGE'.format(self.species, self.name)).center(83))
            return True

    def too_fat(self):
        if self.weight >= self.obesity:
            print('\n', ('{} {} DIED OF OBESITY'.format(self.species, self.name)).center(83))
            return True


class Wolf(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = self.get_gender(gender)
        self.name = self.get_name(self.gender, name)
        self.age = self.get_age(age, 16)
        self.weight = self.get_weight(weight, 0.5, 12)
        self.description = self.get_description(description, 'vegetarian')
        self.species = self.get_species(species, 'wolf')
        self.obesity = self.get_obesity(obesity, 80)
        self.lifespan = self.get_lifespan(lifespan, 75)


class Parrot(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = self.get_gender(gender)
        self.name = self.get_name(self.gender, name)
        self.age = self.get_age(age, 15)
        self.weight = self.get_weight(weight, 0.3, 2)
        self.description = self.get_description(description, 'bites visitors')
        self.species = self.get_species(species, 'parrot')
        self.obesity = self.get_obesity(obesity, 10)
        self.lifespan = self.get_lifespan(lifespan, 65)


class Raven(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = self.get_gender(gender)
        self.name = self.get_name(self.gender, name)
        self.age = self.get_age(age, 25)
        self.weight = self.get_weight(weight, 0.3, 2)
        self.description = self.get_description(description, 'doubts its existence')
        self.species = self.get_species(species, 'raven')
        self.obesity = self.get_obesity(obesity, 9)
        self.lifespan = self.get_lifespan(lifespan, 65)


class Lizard(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = self.get_gender(gender)
        self.name = self.get_name(self.gender, name)
        self.age = self.get_age(age, 28)
        self.weight = self.get_weight(weight, 0.1, 3)
        self.description = self.get_description(description, 'sluggish')
        self.species = self.get_species(species, 'lizard')
        self.obesity = self.get_obesity(obesity, 15)
        self.lifespan = self.get_lifespan(lifespan, 50)


class New(Animal):
    def __init__(self, gender=None, name=None, age=None, weight=None,
                 lifespan=None, obesity=None, description=None, species=None):
        super().__init__()
        self.gender = self.get_gender(gender)
        self.name = self.get_name(self.gender, name)
        self.age = self.get_age(age, 7)
        self.weight = self.get_weight(weight, 0.07, 0.19)
        self.description = self.get_description(description, 'secretive') 
        self.species = self.get_species(species, 'indefinite')
        self.obesity = self.get_obesity(obesity, 12)
        self.lifespan = self.get_lifespan(lifespan, 50)


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
                print('\n ', ('{} {} SWALLOWED UP {} {}'.format(hungry.species, hungry.name,
                                                                food.species, food.name)).center(83))
                hungry.weight += food.weight
                self.array.pop(self.array.index(food))

    def reproduction(self):
        x = random.choice(self.array)
        y = random.choice(self.array)
        if x != y and x.gender != y.gender and abs(x.weight-y.weight) <= min(x.weight, y.weight):
            strength = random.randint(1, 4)
            print('\n', ('{} NEWBORNS!'.format(strength)).center(83))
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


if __name__ == '__main__':
    animals = []
    wolf = Wolf('male', weight=10)
    lizard = Lizard()
    raven = Raven()
    gonzo = Lizard()
    parrot = Parrot()
    animals.append(wolf)
    animals.extend([lizard, lizard, raven, gonzo, parrot])
    zoo = Shop(animals)
    zoo.get_list()

    def time_later(beasts, shop):
        print('\n', 'Some time later'.center(71))
        for beast in beasts:
            beast.aging()
            beast.growth()
            if beast.old_age() or beast.too_fat():
                beasts.pop(beasts.index(beast))
        shop.incident()
        shop.reproduction()
        time.sleep(2)

    while True:
        time_later(animals, zoo)
        zoo.get_list()

