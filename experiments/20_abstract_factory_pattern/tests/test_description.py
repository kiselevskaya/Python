# -*- coding: utf-8 -*-
# test_description.py


import unittest
from factory import *
from decorators import repeat


class NameCheckTestCase(unittest.TestCase):
    def setUp(self):
        self.pet_factory = PetFactory()

    @repeat(50)
    def test_wolf_name_not_none(self):
        wolf = self.pet_factory.create_wolf()
        self.assertIsNotNone(wolf.get_description())

    @repeat(50)
    def test_lizard_name_not_none(self):
        lizard = self.pet_factory.create_lizard()
        self.assertIsNotNone(lizard.get_description())

    @repeat(50)
    def test_raven_name_not_none(self):
        raven = self.pet_factory.create_raven()
        self.assertIsNotNone(raven.get_description())

    @repeat(50)
    def test_parrot_name_not_none(self):
        parrot = self.pet_factory.create_parrot()
        self.assertIsNotNone(parrot.get_description())
