

import unittest


class Warrior(object):
    def __init__(self):
        self.ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.experience = 100
        self.level = 1
        self.rank = "Pushover"
        self.achievements = []
        self.set_experience(100)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def training(self, trainer):
        if self.level >= trainer[2]:
            self.set_experience(self.experience+trainer[1])
            self.set_achievements(trainer[0])
            return trainer[0]
        else:
            return "Not strong enough"

    def set_achievements(self, new_achievement):
        self.achievements.append(new_achievement)

    def battle(self, enemy_level):
        if enemy_level not in range(1, 101):
            return "Invalid level"
        elif self.ranks.index(self.rank) < enemy_level//10 and self.level+5 <= enemy_level:
            return "You've been defeated"
        elif enemy_level > self.level:
            self.set_experience(self.experience+20*(enemy_level-self.level)**2)
            return "An intense fight"
        elif self.level == enemy_level:
            self.set_experience(self.experience+10)
            return "A good fight"
        elif self.level == enemy_level+1:
            self.set_experience(self.experience+5)
            return "A good fight"
        else:
            return "Easy fight"

    def set_experience(self, exp):
        self.experience = exp
        if self.experience > 10000:
            self.experience = 10000
        self.level = self.experience//100
        self.rank = self.ranks[self.experience//1000]


class TestWarrior(unittest.TestCase):
    tom = Warrior()
    bruce_lee = Warrior()

    def test_run_equal(self):
        self.assertEquals(self.tom.level, 1)
        self.assertEquals(self.tom.experience, 100)
        self.assertEquals(self.tom.rank, "Pushover")

        self.assertEquals(self.bruce_lee.level, 1)
        self.assertEquals(self.bruce_lee.experience, 100)
        self.assertEquals(self.bruce_lee.rank, "Pushover")
        self.assertEquals(self.bruce_lee.achievements, [])
        self.assertEquals(self.bruce_lee.training(["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")
        self.assertEquals(self.bruce_lee.experience, 9100)
        self.assertEquals(self.bruce_lee.level, 91)
        self.assertEquals(self.bruce_lee.rank, "Master")
        self.assertEquals(self.bruce_lee.battle(90), "A good fight")
        self.assertEquals(self.bruce_lee.experience, 9105)
        self.assertEquals(self.bruce_lee.achievements, ["Defeated Chuck Norris"])


if __name__ == '__main__':
    unittest.main()
