# -*- coding: utf-8 -*-
# shop_assistant.py


from pet_shop import print_shop


class ShopAssistant:
    def __init__(self, pet_factory, animals_array, shop):
        self.pet_factory = pet_factory
        self.animals_array = animals_array
        self.shop = shop

    def add_animal(self):
        species = str(input('Enter species: '))
        gender = str(input('Enter gender: '))
        name = str(input('Enter animal name: '))
        age = int(input('Enter age in years(float): '))
        weight = float(input('Enter animal weight: '))
        lifespan = int(input('Enter lifespan in years: '))
        obesity = int(input('Enter obesity in kg: '))
        description = str(input('Enter description: '))
        user_animal = self.pet_factory.create_cross_born(species, gender, name, age, weight, lifespan, obesity, description)
        self.animals_array.append(user_animal)

    def choose_options(self):
        user_choice = None
        while user_choice != 0 or user_choice != 1:
            user_choice = int(input('\n Enter 0 to see all animals or 1 to add one more: '))
            if user_choice == 0:
                print_shop(self.shop)
            elif user_choice == 1:
                self.add_animal()
