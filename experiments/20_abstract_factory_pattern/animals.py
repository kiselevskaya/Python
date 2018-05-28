# -*- coding: utf-8 -*-
# animals.py


import random
month = 0.083


class Animal(object):
    def __init__(self, gender, name, age, weight, lifespan, obesity, description, species):
        global month
        self.gender = gender
        self.name = name
        self.age = age
        self.weight = weight
        self.lifespan = lifespan
        self.obesity = obesity
        self.species = species
        self.description = description

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
        self.age += 3*month
        return self.age

    def growth(self):
        self.weight += round(random.uniform(0.2, 0.5), 2)
        return self.weight

    def old_age(self):
        if self.age >= self.lifespan:
            print('\n', '☠RIP☠'.center(83))
            print('\n', ('{} {} was too old'.format(self.species, self.name)).center(83))
            return True

    def too_fat(self):
        if self.weight >= self.obesity:
            print('\n', '☠RIP☠'.center(83))
            print('\n', ('{} {} was too fat'.format(self.species, self.name)).center(83))
            return True


class Wolf(Animal):
    def __init__(self, gender=None, name=None, age=round(random.uniform(month, 16), 2),
                 weight=round(random.uniform(0.5, 16), 2), lifespan=75, obesity=80,
                 description='vegetarian'):
        super().__init__(gender, name, age, weight, lifespan, obesity, description, 'wolf')


class Parrot(Animal):
    def __init__(self, gender, name, age,
                 weight=round(random.uniform(0.3, 2), 2), lifespan=65, obesity=10,
                 description='bites visitors', species='parrot'):
        super().__init__(gender, name, age, weight, lifespan, obesity, description, species)


class Raven(Animal):
    def __init__(self, gender=None, name=None, age=round(random.uniform(month, 15), 2),
                 weight=round(random.uniform(0.3, 2), 2), lifespan=65, obesity=9,
                 description='doubts its existence', species='raven'):
        super().__init__(gender, name, age, weight, lifespan, obesity, description, species)


class Lizard(Animal):
    def __init__(self, gender=None, name=None, age=round(random.uniform(month, 18), 2),
                 weight=round(random.uniform(0.1, 3), 2), lifespan=50, obesity=15,
                 description='sluggish', species='lizard'):
        super().__init__(gender, name, age, weight, lifespan, obesity, description, species)


class CrossBorn(Animal):
    def __init__(self, species, gender=None, name=None, age=round(random.uniform(month, 7), 2),
                 weight=round(random.uniform(0.07, 0.19), 2), lifespan=50, obesity=12,
                 description='secretive'):
        super().__init__(gender, name, age, weight, lifespan, obesity, description, species)


if __name__ == '__main__':
    w = Wolf()
    if w is None:
        print("ERROR")
    else:
        print(w)
