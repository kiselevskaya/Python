# -*- coding: utf-8 -*-
# test_lifespan.py


import unittest
from factory import *
from decorators import repeat


class LifespanTestCase(unittest.TestCase):
    def setUp(self):
        self.pet_factory = PetFactory()

    @repeat(50)
    def test_wolf_lifespan(self):
        wolf = self.pet_factory.create_wolf()
        self.assertGreater(self.pet_factory.wolf_lifespan, wolf.get_age())
        self.assertTrue(wolf.get_lifespan() == self.pet_factory.wolf_lifespan)

    def test_lizard_lifespan(self):
        lizard = self.pet_factory.create_lizard()
        self.assertTrue(lizard.get_age() < self.pet_factory.lizard_lifespan)
        self.assertTrue(lizard.get_lifespan() == self.pet_factory.lizard_lifespan)

    def test_parrot_lifespan(self):
        parrot = self.pet_factory.create_parrot()
        self.assertTrue(parrot.get_age() < self.pet_factory.parrot_lifespan)
        self.assertTrue(parrot.get_lifespan() == self.pet_factory.parrot_lifespan)

    def test_raven_lifespan(self):
        raven = self.pet_factory.create_raven()
        self.assertTrue(raven.get_age() < self.pet_factory.raven_lifespan)
        self.assertTrue(raven.get_lifespan() == self.pet_factory.raven_lifespan)
