# -*- coding: utf-8 -*-
# names.py


import random
import os


class Names:
    def __init__(self, female=None,  # '../00_text_files/female_names.txt',
                 male=None):  # '../00_text_files/male_names.txt'):
        if female is None:
            female = os.path.dirname(os.path.abspath(__file__))+'/../00_text_files/female_names.txt'
        if male is None:
            male = os.path.dirname(os.path.abspath(__file__))+'/../00_text_files/male_names.txt'
        self.female = female
        self.male = male
        self.female_list = None
        self.male_list = None

    def create_female_name(self):
        arr = []
        f = open(self.female, 'rt')
        for name in [l.split('\n') for l in f]:
            arr.append(name[0])
        f.close()
        return random.choice(arr)

    def create_male_name(self):
        arr = []
        f = open(self.male, 'rt')
        for name in [l.split('\n') for l in f]:
            arr.append(name[0])
        f.close()
        return random.choice(arr)

    def create_name(self, gender):
        if gender == 'female':
            return self.create_female_name()
        elif gender == 'male':
            return self.create_male_name()
