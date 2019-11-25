

import unittest


class Warrior():
    def __init__(self):
        self.ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.experience = 100
        if self.experience//100 > 100:
            self.level = 100
        else:
            self.level = self.experience//100
        self.rank = self.ranks[self.level//10]
        self.achievements = []

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def training(self, trainer):
        if self.level >= trainer[2]:
            self.experience += trainer[1]
            self.achievements.append(trainer[0])
            return trainer[0]
        else:
            return "Not strong enough"

    def battle(self, enemy_level):
        if enemy_level not in range(1, 101):
            return "Invalid level"
        elif self.ranks.index(self.rank) < self.ranks.index(self.ranks[enemy_level//10]) and self.level+5 <= enemy_level:
            return "You've been defeated"
        elif enemy_level > self.level:
            self.experience = 20*(enemy_level-self.level)**2
            return "An intense fight"
        elif self.level == enemy_level:
            self.experience += 10
            return "A good fight"
        elif self.level == enemy_level+1:
            self.experience += 5
            return "A good fight"
        else:
            return "Easy fight"


tom = Warrior()
bruce_lee = Warrior()

print(tom.level)   # 1
print(tom.experience)   # 100
print(tom.rank)    # "Pushover"

print(bruce_lee.level)   # 1
print(bruce_lee.experience)   # 100
print(bruce_lee.rank)   # "Pushover"
print(bruce_lee.achievements)   # []
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))   # "Defeated Chuck Norris"
print(bruce_lee.experience)   # 9100

print(bruce_lee.level)  # 91
print(bruce_lee.rank)   # "Master"
print(bruce_lee.battle(90))   # "A good fight"
print(bruce_lee.experience)   # 9105
print(bruce_lee.achievements)   # ["Defeated Chuck Norris"]


# class TestCarMileage(unittest.TestCase):
#
#     def equal_tests(self):
#         tom = Warrior()
#         bruce_lee = Warrior()
#
#         self.assertEquals(tom.level, 1)
#         self.assertEquals(tom.experience, 100)
#         self.assertEquals(tom.rank, "Pushover")
#
#         self.assertEquals(bruce_lee.level, 1)
#         self.assertEquals(bruce_lee.experience, 100)
#         self.assertEquals(bruce_lee.rank, "Pushover")
#         self.assertEquals(bruce_lee.achievements, [])
#         self.assertEquals(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")
#         self.assertEquals(bruce_lee.experience, 9100)
#         self.assertEquals(bruce_lee.level, 91)
#         self.assertEquals(bruce_lee.rank, "Master")
#         self.assertEquals(bruce_lee.battle(90), "A good fight")
#         self.assertEquals(bruce_lee.experience, 9105)
#         self.assertEquals(bruce_lee.achievements, ["Defeated Chuck Norris"])


# if __name__ == '__main__':
#     unittest.main()
