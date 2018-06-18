# -*- coding: utf-8 -*-
# test_shop_incident.py


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


class IncidentTestCase(unittest.TestCase):
    def setUp(self):
        animals = []
        pet_factory = PetFactory()
        wolf = pet_factory.create_wolf()
        lizard = pet_factory.create_lizard()
        raven = pet_factory.create_raven()
        gonzo = pet_factory.create_lizard()
        parrot = pet_factory.create_parrot()
        animals.extend([wolf, lizard, raven, gonzo, parrot])
        self.shop = Shop(pet_factory, animals, RandomIncidentFactoryMock())

    @repeat(10)
    def test_incident_food_not_in_animals(self):
        self.assertEqual(5, len(self.shop.get_animals()))
        self.shop.incident()
        self.assertEqual(4, len(self.shop.get_animals()))
