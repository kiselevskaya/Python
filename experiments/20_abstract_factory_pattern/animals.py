# -*- coding: utf-8 -*-
# animals.py


import random
month = 0.083


class Animal(object):
    def __init__(self, species, gender, name, age, weight, lifespan, obesity, description):
        global month
        self.species = species
        self.gender = gender
        self.name = name
        self.age = age
        self.weight = weight
        self.lifespan = lifespan
        self.obesity = obesity
        self.description = description

    def get_species(self):
        return self.species

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

    def get_obesity(self):
        return self.obesity

    def get_lifespan(self):
        return self.lifespan

    def __repr__(self):
        return ('{}{}{}{}{}{}'.format(str(self.gender).ljust(12), str(self.name).ljust(12),
                                      str(round(self.age, 2)).ljust(12), str(round(self.weight, 2)).ljust(12),
                                      str(self.description).ljust(23), str(self.species).ljust(12)))

    def aging(self):
        self.age += month
        return self.age

    def growth(self):
        self.weight += round(random.uniform(0.2, 0.5), 2)
        return self.weight

    def old_age(self):
        if self.age >= self.lifespan:
            return True

    def too_fat(self):
        if self.weight >= self.obesity:
            return True


class Wolf(Animal):
    def __init__(self, gender, name, age, weight, lifespan, obesity, description):
        super().__init__('wolf', gender, name, age, weight, lifespan, obesity, description)


class Parrot(Animal):
    def __init__(self, gender, name, age, weight, lifespan, obesity, description):
        super().__init__('parrot', gender, name, age, weight, lifespan, obesity, description)


class Raven(Animal):
    def __init__(self, gender, name, age, weight, lifespan, obesity, description):
        super().__init__('raven', gender, name, age, weight, lifespan, obesity, description)


class Lizard(Animal):
    def __init__(self, gender, name, age, weight, lifespan, obesity, description):
        super().__init__('lizard', gender, name, age, weight, lifespan, obesity, description)


class CrossBorn(Animal):
    def __init__(self, species, gender, name, age, weight, lifespan, obesity, description):
        super().__init__(species, gender, name, age, weight, lifespan, obesity, description)
