# 08_is_rotation.py


'''Assume you have a method isSubstring which checks if one word is a substring of another.
    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
    (e.g. 'waterbottle' is a rotation of 'erbottlewat').
'''


def isSubstring(s1, s2):
    if s2 in s1:
        return True
    else:
        return False


def is_rotation(s1, s2):
    if len(s1) != len(s2) or any([len(s1), len(s2)]) < 1:
        return False
    else:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)


if __name__ == '__main__':
    # Test case 0
    s01 = 'waterbottle'
    s02 = 'erbottlewat'
    print(is_rotation(s01, s02))

    # Test case 1
    s11 = 'waterbottle'
    s12 = 'erbottlevat'
    print(is_rotation(s11, s12))

    # Test case 2
    s21 = 'waterottle'
    s22 = 'erbottlewat'
    print(is_rotation(s21, s22))

    # Test case 3
    s31 = 'waterbottle'
    s32 = 'ebottlewat'
    print(is_rotation(s31, s32))

    # Test case 4
    s41 = 'waterbottle'
    s42 = 'erbottlewate'
    print(is_rotation(s41, s42))
