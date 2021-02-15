# insert_number.py

"""
Given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and end at bit i.

clear j-i bits of N
shift M on i
merge N and M
"""


def insert_number(n, m, i, j):
    ones = int('1' * n.bit_length(), 2)       # ~0
    left = ones << (j+1)      # left part of mask
    right = ((1 << i)-1)    # right part of mask
    mask = left | right     # mask contains all 1s except 0s on positions j through i

    n = (n & mask)      # clear bits j through i
    m = m << i      # shift M on i position left ... and merge N with M
    return bin(n | m)[2:]


if __name__ == '__main__':
    t1 = int('10000000000', 2)
    m1 = int('10011', 2)
    i1, j1 = 2, 6
    t2 = int('0100011100', 2)
    t3 = int('0000011100', 2)
    t4 = int('1111111111', 2)

    print(insert_number(t4, m1, i1, j1))
