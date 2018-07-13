# -*- coding: utf-8 -*-
# pet_shop.py


import random
import time
import json
from collections import OrderedDict


class AbstractRandomFactory(object):
    def choice(self, array):
        pass


class RealRandomFactory(AbstractRandomFactory):
    def choice(self, array):
        return random.choice(array)


class Shop:
    def __init__(self, pet_factory, animals_array, random_factory=RealRandomFactory()):
        self.logs = []
        self.pet_factory = pet_factory
        self.animals_array = animals_array
        self.random_factory = random_factory
        self.title = ('{}{}{}{}{}{}'.format('Gender'.ljust(12),
                                            'Name'.ljust(12),
                                            'Age(years)'.ljust(12),
                                            'Weight(kg)'.ljust(12),
                                            'Description'.ljust(23),
                                            'Species'.ljust(12)))

    def get_animals(self):
        return self.animals_array

    def get_logs(self):
        return self.logs

    def incident(self):
        if len(self.animals_array) >= 2:
            hungry = self.random_factory.choice(self.animals_array)
            food = self.random_factory.choice(self.animals_array)
            if hungry != food and hungry.weight >= (food.weight*2):
                hungry.weight += food.weight
                localtime = time.asctime(time.localtime(time.time()))
                log = '{} {} swallowed up {} {}'.format(hungry.species, hungry.name, food.species, food.name)
                self.animals_array.pop(self.animals_array.index(food))
                self.logs.append([localtime, log])

    def reproduction(self):
        if len(self.animals_array) >= 2:
            x = self.random_factory.choice(self.animals_array)
            y = self.random_factory.choice(self.animals_array)
            if x != y and x.gender != y.gender and abs(x.weight-y.weight) <= min(x.weight, y.weight):
                strength = random.randint(3, 7)
                localtime = time.asctime(time.localtime(time.time()))
                log = '{} {} & {} {} have {} newborns'.format(x.species, x.name, y.species, y.name, strength)
                self.logs.append([localtime, log])
                num = 0
                while num != strength:
                    num += 1
                    if x.species == y.species:
                        species = x.species
                    else:
                        species = '{}-{}'.format(x.species, y.species)
                    lifespan = sum([x.lifespan, y.lifespan]) // 2
                    obesity = sum([x.obesity, y.obesity]) // 2
                    description = random.choice([x.description, y.description])
                    newborn = self.pet_factory.create_cross_born(species=species,
                                                                 lifespan=lifespan,
                                                                 obesity=obesity,
                                                                 description=description)
                    self.animals_array.append(newborn)

    def ticker(self):
        animals = self.animals_array
        for animal in animals:
            animal.aging()
            animal.growth()
            if animal.old_age():
                localtime = time.asctime(time.localtime(time.time()))
                log = 'RIP {} {} was {} years old, it was too old for {}.'.format(animal.species, animal.name, round(animal.age, 2), animal.species)
                self.logs.append([localtime, log])
                animals.pop(animals.index(animal))
            elif animal.too_fat():
                localtime = time.asctime(time.localtime(time.time()))
                log = 'RIP {} {} weighted {} kg, it was too fat for {}.'.format(animal.species, animal.name, round(animal.weight, 2), animal.species)
                self.logs.append([localtime, log])
                animals.pop(animals.index(animal))
        if random.randint(1, 10) % 2 == 0:
            self.incident()
        self.reproduction()


def print_shop(shop):
    localtime = time.asctime(time.localtime(time.time()))
    print(json.dumps(localtime, indent=4))
    for i in shop.get_animals():
        keys = ['species', 'gender', 'name', 'age', 'weight', 'lifespan', 'obesity', 'description']
        values = [i.species, i.gender, i.name, i.age, i.weight, i.lifespan, i.obesity, i.description]
        dictionary = dict(zip(keys, values))
        print(json.dumps(OrderedDict(dictionary), indent=4))

    for log in shop.get_logs():
        keys = ['localtime', 'log']
        values = [log[0], log[1]]
        logs = dict(zip(keys, values))
        print(json.dumps(OrderedDict(logs), indent=4))
