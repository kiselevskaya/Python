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

    def create_cross_born(self, species, lifespan, obesity, description):
        pass


class PetFactory(AbstractFactory):
    def __init__(self):
        self.species = 'undefined'
        self.gender = None
        self.name = None
        self.min_age = 1
        self.max_age = 7
        self.min_weight = 0.1
        self.max_weight = 3
        self.lifespan = 50
        self.obesity = 9
        self.description = 'bites'
        self.names_factory = Names()

        self.wolf_max_age = 18
        self.lizard_max_age = 12
        self.parrot_max_age = 16
        self.raven_max_age = 12

        self.wolf_min_weight = 0.5
        self.wolf_max_weight = 16

        self.lizard_min_weight = 0.1
        self.lizard_max_weight = 1.2

        self.parrot_min_weight = 0.3
        self.parrot_max_weight = 2

        self.raven_min_weight = 0.2
        self.raven_max_weight = 1.6

        self.cross_born_min_weight = 0.07
        self.cross_born_max_weight = 0.19

        self.wolf_lifespan = 75
        self.lizard_lifespan = 50
        self.parrot_lifespan = 65
        self.raven_lifespan = 50

        self.wolf_obesity = 80
        self.lizard_obesity = 15
        self.parrot_obesity = 9
        self.raven_obesity = 8

        self.wolf_description = 'vegetarian'
        self.lizard_description = 'sluggish'
        self.parrot_description = 'bites visitors'
        self.raven_description = 'sluggish'

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
        gender = random.choice(('male', 'female'))
        name = self.names_factory.create_name(gender)

        return Wolf(gender=gender,
                    name=name,
                    age=round(random.uniform(month, self.wolf_max_age), 2),
                    weight=round(random.uniform(self.wolf_min_weight, self.wolf_max_weight), 2),
                    lifespan=self.wolf_lifespan,
                    obesity=self.wolf_obesity,
                    description=self.wolf_description)

    def create_lizard(self):
        gender = random.choice(('male', 'female'))
        name = self.names_factory.create_name(gender)

        return Lizard(gender=gender,
                      name=name,
                      age=round(random.uniform(month, self.lizard_max_age), 2),
                      weight=round(random.uniform(self.lizard_min_weight, self.lizard_max_weight), 2),
                      lifespan=self.lizard_lifespan,
                      obesity=self.lizard_obesity,
                      description=self.lizard_description)

    def create_parrot(self):
        gender = random.choice(('male', 'female'))
        name = self.names_factory.create_name(gender)

        return Parrot(gender=gender,
                      name=name,
                      age=round(random.uniform(month, self.parrot_max_age), 2),
                      weight=round(random.uniform(self.parrot_min_weight, self.parrot_max_weight), 2),
                      lifespan=self.parrot_lifespan,
                      obesity=self.parrot_obesity,
                      description=self.parrot_description)

    def create_raven(self):
        gender = random.choice(('male', 'female'))
        name = self.names_factory.create_name(gender)

        return Raven(gender=gender,
                     name=name,
                     age=round(random.uniform(month, self.raven_max_age), 2),
                     weight=round(random.uniform(self.raven_min_weight, self.raven_max_weight), 2),
                     lifespan=self.raven_lifespan,
                     obesity=self.raven_obesity,
                     description=self.raven_description)

    def create_cross_born(self, species, lifespan, obesity, description):
        gender = random.choice(('male', 'female'))
        name = self.names_factory.create_name(gender)

        return CrossBorn(species=species,
                         gender=gender,
                         name=name,
                         age=0,
                         weight=round(random.uniform(self.cross_born_min_weight, self.cross_born_max_weight), 2),
                         lifespan=lifespan,
                         obesity=obesity,
                         description=description)


def pet_factory_tests():
    pet_factory = PetFactory()
    wlf = pet_factory.create_wolf()
    prt = pet_factory.create_parrot()
    print(wlf)
    print(prt)


if __name__ == '__main__':
    pet_factory_tests()
