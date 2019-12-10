

import random


_actions = [lambda x:x+1, lambda x:0, lambda x: x/2, lambda x: x*100, lambda x: x%2]


class Machine:
    def __init__(self):
        # self.actions = ACTIONS()
        self.actions = _actions
        self.cmd = None
        self.commands = {}
        for act in range(len(self.actions)):
            self.commands[act] = len(self.actions)-1

    def command(self, cmd, num):
        self.cmd = cmd
        print('{} command applying on number {} gives result {}'.format(cmd, num, self.actions[self.cmd](num)))
        return self.actions[self.commands[cmd]](num)

    def response(self, res):
        if not res:
            self.commands[self.cmd] = (self.commands[self.cmd]+1) % len(self.actions)
            return
        print('Command {} refer to index {}'.format(self.cmd, self.commands[self.cmd]))
        print()
        return self.commands[self.cmd]


machine = Machine()

print('FIRST***********************************************************************************************************')
random.seed()
for i in range(0, 20):
    r = machine.command(0, random.randint(0, 100))
    machine.response(r == 0)

assert machine.command(0, random.randint(0, 100)) == 0, 'Should be 0'

tests = [(0, 100, 101, "Should apply the num + 1 action to the command 0"),
         (1, 100, 0, "Should apply the num * 0 action to the command 1"),
         (2, 100, 50, "Should apply the num / 2 action to the command 2"),
         (3, 1, 100, "Should apply the num * 100 action to the command 3"),
         (4, 100, 0, "Should apply the num % 2 action to the command 4")]

print()
print('SECOND**********************************************************************************************************')
for i in range(0, 20):
    number = random.randint(0, 100)
    num = machine.command(i % 5, number)
    machine.response(_actions[i % 5](number) == num)

print()
print('THIRD************************************************************************************************************')
for t in tests:
    num = machine.command(t[0], t[1])
    assert num == t[2], [t[3], 'num {} is not {}'.format(num, t[2])]
