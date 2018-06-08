# -*- coding: utf-8 -*-
# test_factory.py


import unittest
from factory import *
from decorators import repeat


class AgeLimitTestCase(unittest.TestCase):
    pet_factory = PetFactory()

    @repeat(5)
    def test_wolf_gender_not_none(self):
        wolf = self.pet_factory.create_wolf()
        self.assertIsNotNone(wolf.get_gender)

    @repeat(5)
    def test_lizard_gender_not_none(self):
        lizard = self.pet_factory.create_lizard()
        self.assertIsNotNone(lizard.get_gender)

    @repeat(5)
    def test_raven_gender_not_none(self):
        raven = self.pet_factory.create_raven()
        self.assertIsNotNone(raven.get_gender)

    @repeat(5)
    def test_parrot_gender_not_none(self):
        parrot = self.pet_factory.create_parrot()
        self.assertIsNotNone(parrot.get_gender)

    def test_wolf_name_not_none(self):
        wolf = self.pet_factory.create_wolf()
        self.assertIsNotNone(wolf.get_name)

    def test_lizard_name_not_none(self):
        lizard = self.pet_factory.create_lizard()
        self.assertIsNotNone(lizard.get_name)

    def test_raven_name_not_none(self):
        raven = self.pet_factory.create_raven()
        self.assertIsNotNone(raven.get_name)

    def test_parrot_name_not_none(self):
        parrot = self.pet_factory.create_parrot()
        self.assertIsNotNone(parrot.get_name)

    def test_check_min_age(self):
        self.assertEqual(self.pet_factory.min_age, month)

    def test_check_wolf_age(self):
        wolf = self.pet_factory.create_wolf()
        self.assertTrue(wolf.get_age() <= self.pet_factory.wolf_max_age)
        self.assertTrue(wolf.get_age() >= self.pet_factory.min_age)

    def test_check_lizard_age(self):
        lizard = self.pet_factory.create_lizard()
        self.assertTrue(lizard.get_age() <= self.pet_factory.lizard_max_age)

    def test_check_parrot_age(self):
        parrot = self.pet_factory.create_parrot()
        self.assertTrue(parrot.get_age() <= self.pet_factory.parrot_max_age)

    def test_check_raven_age(self):
        raven = self.pet_factory.create_raven()
        self.assertTrue(raven.get_age() <= self.pet_factory.raven_max_age)
