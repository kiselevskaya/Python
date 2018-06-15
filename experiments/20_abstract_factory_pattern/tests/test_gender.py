# -*- coding: utf-8 -*-
# test_gender.py


import unittest
from factory import *
from decorators import repeat


class GenderCheckTestCase(unittest.TestCase):
    def setUp(self):
        self.pet_factory = PetFactory()

    @repeat(50)
    def test_wolf_gender_not_none(self):
        wolf = self.pet_factory.create_wolf()
        self.assertIsNotNone(wolf.get_gender)

    @repeat(50)
    def test_lizard_gender_not_none(self):
        lizard = self.pet_factory.create_lizard()
        self.assertIsNotNone(lizard.get_gender)

    @repeat(50)
    def test_raven_gender_not_none(self):
        raven = self.pet_factory.create_raven()
        self.assertIsNotNone(raven.get_gender)

    @repeat(50)
    def test_parrot_gender_not_none(self):
        parrot = self.pet_factory.create_parrot()
        self.assertIsNotNone(parrot.get_gender)
