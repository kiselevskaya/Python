

import re


PATTERN = re.compile(r"^(0*)((1(0(1)*0)*1)*0*)*$")

tests = [(False, " 0"),
    (False, "abc"),
    (True,  "000"),
    (True,  "110110"),
    (False, "111"),
    (True,  "{:b}".format(12345678)),
    ]

for exp, s in tests:
    if bool(PATTERN.match(s)) != exp:
        print("Should work with '{}'".format(s))


# def multipleof3Regex(n):
#     try:
#         return int(n, 2) % 3 == 0
#     except:
#         return False
#     # lst = list(n)
#     # if lst not in [{'0', '1'}, {'1'}, {'0'}]:
#     #     return False
#     # state = 0
#     # for i in range(len(lst)):
#     #     digit = int(lst[i])
#     #     if state == 0:
#     #         if digit == 1:
#     #             state = 1
#     #             continue
#     #     if state == 1:
#     #         if digit == 0:
#     #             state = 2
#     #         else:
#     #             state = 0
#     #     if state == 2:
#     #         if digit == 0:
#     #             state = 1
#     # if state == 0:
#     #     return True
#     # return False


# print(multipleof3Regex(' 0'))   # False
# print(multipleof3Regex('110a'))   # False
# print(multipleof3Regex('1'))   # False
# print(multipleof3Regex('101'))   # False
# print(multipleof3Regex('111'))   # False
# print(multipleof3Regex('1000'))   # False
# print(multipleof3Regex('1010'))   # False
# print(multipleof3Regex('1011'))   # False
# print(multipleof3Regex('1101'))   # False
# print(multipleof3Regex('1110'))   # False
# print(multipleof3Regex('10000'))   # False
# print(multipleof3Regex('abc'))   # False
# print(multipleof3Regex('000'))  # True
# print(multipleof3Regex('110'))  # True
# print(multipleof3Regex('111'))   # False
# print(multipleof3Regex('{:b}'.format(12345678)))  # True
