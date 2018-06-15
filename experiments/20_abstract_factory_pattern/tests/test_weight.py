# -*- coding: utf-8 -*-
# test_weight.py


import unittest
from factory import *
from decorators import repeat


class WeightLimitTestCase(unittest.TestCase):
    def setUp(self):
        self.pet_factory = PetFactory()

    @repeat(150)
    def test_check_wolf_weight(self):
        wolf = self.pet_factory.create_wolf()
        self.assertTrue(wolf.get_weight() <= self.pet_factory.wolf_max_weight)
        self.assertTrue(wolf.get_weight() >= self.pet_factory.wolf_min_weight)

    @repeat(50)
    def test_check_lizard_weight(self):
        lizard = self.pet_factory.create_lizard()
        self.assertTrue(lizard.get_weight() <= self.pet_factory.lizard_max_weight)
        self.assertTrue(lizard.get_weight() >= self.pet_factory.lizard_min_weight)

    def test_check_parrot_weight(self):
        parrot = self.pet_factory.create_parrot()
        self.assertTrue(parrot.get_weight() <= self.pet_factory.parrot_max_weight)
        self.assertTrue(parrot.get_weight() >= self.pet_factory.parrot_min_weight)

    def test_check_raven_weight(self):
        raven = self.pet_factory.create_raven()
        self.assertTrue(raven.get_weight() <= self.pet_factory.raven_max_weight)
        self.assertTrue(raven.get_weight() >= self.pet_factory.raven_min_weight)
