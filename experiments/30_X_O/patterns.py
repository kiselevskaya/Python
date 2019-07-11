

import re


class Patterns:
    def __init__(self):
        self.pattern = [[], [], []]
        self.directions = []
        self.pre_patterns = [{'v': 10000, 'p': ['xxxxx']},
                             {'v': 1000, 'p': ['0xxxx0']},
                             {'v': 500, 'p': ['xxxx0']},
                             {'v': 400, 'p': ['x0xxx', 'xx0xx']},
                             {'v': 100, 'p': ['00xxx000']},
                             {'v': 80, 'p': ['00xxx00']},
                             {'v': 75, 'p': ['0xxx00']},
                             {'v': 50, 'p': ['0xxx0', 'xxx00']},
                             {'v': 25, 'p': ['x0xx0', 'xx0x0', 'x00xx']},
                             {'v': 10, 'p': ['000xx000']},
                             {'v': 5, 'p': ['0xx0']}
                             ]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def get_patterns(self):
        for i in range(len(self.pre_patterns)):
            a = []
            for e in self.pre_patterns[i]['p']:
                # print(e)
                for z in range(len(e)):
                    try:
                        a.append(e[:z]+'7'+e[z+1:])
                    except IndexError:
                        continue

            self.pattern[0].append(self.pre_patterns[i]['v'])
            self.pattern[1].append(re.sub('[x]', '1', '|'.join(a)))
            self.pattern[2].append(re.sub('[x]', '2', '|'.join(a)))
        print(self.pattern)
        return self.pattern

    def potential_step(self):
        pass
