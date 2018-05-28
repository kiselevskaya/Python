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

    def get_animals(self):
        return self.animals_array

    # make separate file
    def add_animal(self):
        species = str(input('Enter species: '))
        gender = str(input('Enter gender: '))
        name = str(input('Enter animal name: '))
        age = int(input('Enter age in years(float): '))
        weight = float(input('Enter animal weight: '))
        lifespan = int(input('Enter lifespan in years: '))
        obesity = int(input('Enter obesity in kg: '))
        description = str(input('Enter description: '))
        new = self.pet_factory.create_cross_born(species, gender, name, age, weight, lifespan, obesity, description)
        self.animals_array.append(new)

    def choose_options(self):
        user_choice = None
        while user_choice != 0 or user_choice != 1:
            user_choice = int(input('\n Enter 0 to see all animals or 1 to add one more: '))
            if user_choice == 0:
                self.get_list()
            elif user_choice == 1:
                self.add_animal()

    def incident(self):
        if len(self.animals_array) >= 2:
            hungry = random.choice(self.animals_array)
            food = random.choice(self.animals_array)
            if hungry != food and hungry.weight >= (food.weight*2):
                hungry.weight += food.weight
                print('\n ', ('{} {} ♻ swallowed up ♻ {} {}'.format(hungry.species, hungry.name,
                                                                    food.species, food.name)).center(83))
                self.animals_array.pop(self.animals_array.index(food))

    def reproduction(self):
        x = random.choice(self.animals_array)
        y = random.choice(self.animals_array)
        if x != y and x.gender != y.gender and abs(x.weight-y.weight) <= min(x.weight, y.weight):
            strength = random.randint(1, 4)
            print('\n', ('{} ※ newborns ※'.format(strength)).center(83))
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
            if animal.old_age() or animal.too_fat():
                animals.pop(animals.index(animal))  # to check
        self.incident()
        self.reproduction()


def print_shop(shop):
    print('\n', shop.title, '\n')
    for i in shop.get_animals():
        print(i)


def simulate(shop):
    while True:
        print('\n', 'Some time later'.center(83))
        shop.ticker()
        time.sleep(2)
        print_shop(shop)


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
    shop = Shop(pet_factory, animals)
    print_shop(shop)
    simulate(shop)


if __name__ == '__main__':
    main()
