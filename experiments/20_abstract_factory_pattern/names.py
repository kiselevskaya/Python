# -*- coding: utf-8 -*-
# names.py


import random


class Names:
    def __init__(self, female='../00_text_files/female_names.txt',
                 male='../00_text_files/male_names.txt'):
        self.female = female
        self.male = male
        self.female_list = None
        self.male_list = None

    def create_female_name(self):
        arr = []
        for name in [l.split('\n') for l in open(self.female, 'rt')]:
            arr.append(name[0])
        return random.choice(arr)

    def create_male_name(self):
        arr = []
        for name in [l.split('\n') for l in open(self.male, 'rt')]:
            arr.append(name[0])
        return random.choice(arr)

    def create_name(self, gender):
        if gender == 'female':
            return self.create_female_name()
        elif gender == 'male':
            return self.create_male_name()
