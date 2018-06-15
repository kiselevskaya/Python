# -*- coding: utf-8 -*-
# test_obesity.py


import unittest
from factory import *
from decorators import repeat


class NameCheckTestCase(unittest.TestCase):
    def setUp(self):
        self.pet_factory = PetFactory()

    @repeat(50)
    def test_wolf_name_not_none(self):
        wolf = self.pet_factory.create_wolf()
        self.assertGreater(wolf.get_obesity(), wolf.get_weight())

    @repeat(50)
    def test_lizard_name_not_none(self):
        lizard = self.pet_factory.create_lizard()
        self.assertGreater(lizard.get_obesity(), lizard.get_weight())

    @repeat(50)
    def test_raven_name_not_none(self):
        raven = self.pet_factory.create_raven()
        self.assertGreater(raven.get_obesity(), raven.get_weight())

    @repeat(50)
    def test_parrot_name_not_none(self):
        parrot = self.pet_factory.create_parrot()
        self.assertGreater(parrot.get_obesity(), parrot.get_weight())
