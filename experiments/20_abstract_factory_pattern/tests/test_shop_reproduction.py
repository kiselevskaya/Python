# -*- coding: utf-8 -*-
# test_shop_reproduction.py


import unittest
from pet_shop import *
from factory import *
from decorators import repeat


class RandomIncidentFactoryMock(AbstractRandomFactory):
    def __init__(self):
        self.call_count = 0

    def choice(self, array):
        self.call_count += 1
        if self.call_count == 1:
            return array[0]
        if self.call_count == 2:
            return array[1]


class ReproductionTestCase(unittest.TestCase):
    def setUp(self):
        animals = []
        pet_factory = PetFactory()
        wolf = pet_factory.create_wolf()
        lizard = pet_factory.create_lizard()
        raven = Raven('male', 'Karl', 2, 1.9, 60, 8, 'bites')
        gonzo = pet_factory.create_lizard()
        parrot = Parrot('female', 'Klara', 1.5, 1.4, 60, 6, 'bites')
        animals.extend([raven, parrot, wolf, lizard,  gonzo])
        self.shop = Shop(pet_factory, animals, RandomIncidentFactoryMock())

    @repeat(10)
    def test_reproduction(self):
        self.setUp()
        self.assertEqual(5, len(self.shop.get_animals()))
        self.shop.reproduction()
        self.assertGreater(len(self.shop.get_animals()), 5)
