# -*- coding: utf-8 -*-
# factory.py


from animals import *
from names import *
import random


class AbstractFactory(object):
    def create_wolf(self):
        pass

    def create_lizard(self):
        pass

    def create_parrot(self):
        pass

    def create_raven(self):
        pass

    def create_crossborn(self, species, lifespan, obesity, description):
        pass


class PetFactory(AbstractFactory):
    def __init__(self):
        self.gender = None
        self.name = None
        self.min_age = 2
        self.max_age = 8
        self.min_weight = 0.1
        self.max_weight = 3
        self.lifespan = 17
        self.obesity = 15
        self.species = 'undefined'
        self.description = 'bites'
        self.names_factory = Names()

    def set_male_gender(self):
        self.gender = 'male'

    def set_female_gender(self):
        self.gender = 'female'

    def set_name(self, name):
        self.name = name

    def set_min_age(self, n):
        self.min_age = n

    def set_max_age(self, x):
        self.max_age = x

    def set_min_weight(self, n):
        self.min_weight = n

    def set_max_weight(self, x):
        self.max_weight = x

    def set_lifespan(self, limit):
        self.lifespan = limit

    def set_obesity(self, limit):
        self.obesity = limit

    def set_species(self, species):
        self.species = species

    def set_description(self, description):
        self.description = description

    def create_wolf(self):
        return Wolf('male',
                    weight=6,
                    age=round(random.uniform(self.min_age, self.max_age), 2))

    def create_lizard(self):
        return Lizard()

    def create_parrot(self):
        gender = random.choice(('male', 'female'))
        name = self.names_factory.create_name(self.gender)

        return Parrot(gender=gender,
                      name=name,
                      age=round(random.uniform(month, 13), 2))

    def create_raven(self):
        return Raven()

    def create_crossborn(self, species, lifespan, obesity, description):
        return CrossBorn(species=species, lifespan=lifespan, obesity=obesity, description=description, age=0)


def pet_factory_tests():
    pet_factory = PetFactory()
    pet_factory.set_min_age(5)
    wlf = pet_factory.create_wolf()
    prt = pet_factory.create_parrot()
    print(wlf)
    print(prt)


if __name__ == '__main__':
    pet_factory_tests()
