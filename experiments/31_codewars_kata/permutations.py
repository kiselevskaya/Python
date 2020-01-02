

import itertools


def permutations(string):
    perm = list(itertools.permutations(string))
    for i in range(len(perm)):
        perm[i] = ''.join(perm[i])
    return list(set(perm))


# def permutations(string):
#     output = []
#     elements = list(string)
#     if len(elements) <= 1:
#         return elements
#     else:
#         for perm in permutations(elements[1:]):
#             for i in range(len(elements)):
#                 output.append(perm[:i] + ''.join(elements[0:1]) + perm[i:])
#     output = list(set(output))
#     return output


print(permutations('a'))
print(permutations('ab'))
print(permutations('aabb'))
