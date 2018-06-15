# -*- coding: utf-8 -*-
# test_age.py


import unittest
from factory import *
from decorators import repeat


class AgeLimitTestCase(unittest.TestCase):
    def setUp(self):
        self.pet_factory = PetFactory()

    @repeat(50)
    def test_check_min_age(self):
        self.assertEqual(self.pet_factory.min_age, month)

    @repeat(50)
    def test_check_wolf_age(self):
        wolf = self.pet_factory.create_wolf()
        self.assertTrue(wolf.get_age() < self.pet_factory.wolf_max_age)
        self.assertTrue(wolf.get_age() >= self.pet_factory.min_age)

    @repeat(50)
    def test_check_lizard_age(self):
        lizard = self.pet_factory.create_lizard()
        self.assertTrue(lizard.get_age() < self.pet_factory.lizard_max_age)
        self.assertTrue(lizard.get_age() >= self.pet_factory.min_age)

    @repeat(50)
    def test_check_parrot_age(self):
        parrot = self.pet_factory.create_parrot()
        self.assertTrue(parrot.get_age() < self.pet_factory.parrot_max_age)
        self.assertTrue(parrot.get_age() >= self.pet_factory.min_age)

    @repeat(50)
    def test_check_raven_age(self):
        raven = self.pet_factory.create_raven()
        self.assertTrue(raven.get_age() < self.pet_factory.raven_max_age)
        self.assertTrue(raven.get_age() >= self.pet_factory.min_age)
