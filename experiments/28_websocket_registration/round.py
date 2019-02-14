

class UserRound:
    def __init__(self):
        self.hit = 0
        self.missed = 0


class Round:
    def __init__(self, image):
        self.hit_by_level = 3
        self.level = 1
        self.user_rounds = dict()
        self.image = image

    def win(self, username):
        if self.user_rounds[username].hit == 3*self.hit_by_level:
            return True
        return False

    def hit(self, username):
        if username not in self.user_rounds:
            self.user_rounds[username] = UserRound()
        self.user_rounds[username].hit += 1
        if self.user_rounds[username].hit == self.level*self.hit_by_level:
            if self.level < 10:
                self.level += 1
            else:
                self.level = 10
            return True
        return False

    def miss(self, username):
        if username not in self.user_rounds:
            self.user_rounds[username] = UserRound()
        self.user_rounds[username].missed += 1
        if self.user_rounds[username].missed == 5:
            return True
        return False
