# swap_even_odd.py


"""
Write a program to swap odd and even bits in an integer with as few instruction as possible
"""


def swap(n):
    mask = int('10'*(int(n.bit_length() / 2 + 0.5)), 2)     # alternation 1 and 0
    left = mask & n     # value of every other bit (starting from the first) alternating in 0
    right = (mask & (n << 1)) << 1      # value of every other bit (starting from the second) alternating in 0
    c = (left | right) >> 1     # interchange even and odd bits and cut the extra 0 on the right
    return bin(c)[2:]


if __name__ == '__main__':
    assert swap(int('10100110', 2)) == '1011001', '1011001 Expected'
    assert swap(int('101', 2)) == '1010', '1010 Expected'
    assert swap(int('10100', 2)) == '101000', '101000 Expected'
    assert swap(int('100', 2)) == '1000', '1000 Expected'
