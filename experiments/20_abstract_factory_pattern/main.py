# -*- coding: utf-8 -*-
# main.py


# from shop_assistant import *
from factory import *
from pet_shop import *
import time


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
    animals.extend([wolf, lizard, raven, gonzo, parrot])
    shop = Shop(pet_factory, animals)
    print_shop(shop)
    simulate(shop)

    # user = ShopAssistant(pet_factory, animals, shop)
    # user.choose_options()


if __name__ == '__main__':
    main()
