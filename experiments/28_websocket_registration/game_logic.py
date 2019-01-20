import random
import string


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class GameLogic:

    def __init__(self):
        self.users = dict()

    def add_user(self, username):
        if username in self.users:
            return None

        password = self.generate_password(username)
        user = User(username, password)
        self.users[username] = user

        return password

    def check_user(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password:
                return True
        return False

    @staticmethod
    def generate_password(username):
        return username + ''.join(random.choices(string.ascii_uppercase + string.digits, k=40))


if __name__ == '__main__':
    import unittest

    class GameLogicTest(unittest.TestCase):
        def testAddUser(self):
            game_logic = GameLogic()
            self.assertIsNotNone(game_logic.add_user("Bobrick"))
            self.assertIsNone(game_logic.add_user("Bobrick"))
            self.assertIsNotNone(game_logic.add_user("Lasto"))
            self.assertIsNone(game_logic.add_user("Lasto"))

        def testCheckUser(self):
            game_logic = GameLogic()
            password = game_logic.add_user("Bobrick")
            self.assertTrue(game_logic.check_user("Bobrick", password))
            self.assertFalse(game_logic.check_user("Bobrick", "D" + password))
            self.assertFalse(game_logic.check_user("Bobrick", ""))

    unittest.main()
