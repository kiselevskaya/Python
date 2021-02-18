# bits_to_convert.py

"""
Write the function to determine the number of bits required to convert integer A to integer B.
"""


def bits_to_convert(a, b):
    result = 0
    xor = a ^ b
    for i in range(xor.bit_length()):
        if bin(xor)[2:][i] == '1':
            result += 1
    return result


if __name__ == '__main__':
    assert bits_to_convert(31, 14) == 2, '2 Expected'
    assert bits_to_convert(72, 14) == 3, '3 Expected'
    assert bits_to_convert(8, 999) == 9, '9 Expected'
    assert bits_to_convert(-8, 17) == 3, '3 Expected'


