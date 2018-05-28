# -*- coding: utf-8 -*-
# pet_shop.py


from factory import *
import random
import time


class Shop:
    def __init__(self, pet_factory, animals_array):
        self.pet_factory = pet_factory
        self.animals_array = animals_array
        self.title = ('{}{}{}{}{}{}'.format('Gender'.ljust(12),
                                            'Name'.ljust(12),
                                            'Age(years)'.ljust(12),
                                            'Weight(kg)'.ljust(12),
                                            'Description'.ljust(23),
                                            'Species'.ljust(12)))

    def get_list(self):
        print('\n', self.title, '\n')
        for i in self.animals_array:
            print(i)

    def get_animals(self):
        return self.animals_array

    def add_animal(self):
        gender = str(input('Enter gender: '))
        name = str(input('Enter animal name: '))
        age = int(input('Enter age in years: '))
        weight = float(input('Enter animal weight: '))
        lifespan = int(input('Enter lifespan in years: '))
        obesity = int(input('Enter obesity in kg: '))
        description = str(input('Enter description: '))
        species = str(input('Enter species: '))
        new = self.pet_factory.create_crossborn(gender, name, age, weight, lifespan, obesity, description, species)
        self.animals_array.append(new)

    def choose_options(self):
        x = None
        while x != 0 or x != 1:
            x = int(input('\n Enter 0 to see all animals or 1 to add one more: '))
            if x == 0:
                self.get_list()
            elif x == 1:
                self.add_animal()

    def incident(self):
        if len(self.animals_array) >= 2:
            hungry = random.choice(self.animals_array)
            food = random.choice(self.animals_array)
            if hungry != food and hungry.weight >= (food.weight*2):
                print('\n ', ('{} {} ♻ SWALLOWED UP ♻ {} {}'.format(hungry.species, hungry.name,
                                                                    food.species, food.name)).center(83))
                hungry.weight += food.weight
                self.animals_array.pop(self.animals_array.index(food))

    def reproduction(self):
        x = random.choice(self.animals_array)
        y = random.choice(self.animals_array)
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
                new = self.pet_factory.create_crossborn(lifespan=max_age,
                                                        obesity=fatness,
                                                        description=feature,
                                                        species=kind)
                self.animals_array.append(new)


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
    pet_factory = PetFactory()
    wolf = pet_factory.create_wolf()
    lizard = pet_factory.create_lizard()
    raven = pet_factory.create_raven()
    gonzo = pet_factory.create_lizard()
    parrot = pet_factory.create_parrot()
    animals.append(wolf)
    animals.extend([lizard, raven, gonzo, parrot])
    zoo = Shop(pet_factory, animals)
    zoo.get_list()
    simulate(zoo)


if __name__ == '__main__':
    main()
