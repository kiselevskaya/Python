# same_one_bits.py


"""
Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.
"""


def non_trailing_zero(n):
    n = bin(n)[2:]
    count = 0       # count for 1 before first non-trailing 0
    one = False
    for i in range(len(n)-1, -1, -1):
        if n[i] == '1':
            count += 1
            if not one:
                one = True
        if one and n[i] == '0':
            return i, count
    return None, count


def last_trailing_zero(n):
    n = bin(n)[2:]
    zero = False
    for i in range(len(n)-1, -1, -1):
        if n[i] == '0':
            if not zero:
                zero = True
        if zero and n[i] == '1':
            return i+1
    return


def flip_zero(n, p):
    left = int(p*'1', 2) << n.bit_length()-p
    right = int(n.bit_length()*'1', 2) >> p+1
    mask = (int(n.bit_length()*'1', 2)) ^ (left | right)
    return mask


def next_larger(n):
    mask = False
    # step 1 flip non-trailing 0 to 1
    pos, ones = non_trailing_zero(n)[0], non_trailing_zero(n)[1]
    # if all bits are 1
    if pos is None:
        mask = int('1', 2) << n.bit_length()+1
        n = mask | n
        pos, ones = non_trailing_zero(n)[0], non_trailing_zero(n)[1]
    flipped = n ^ flip_zero(n, pos)    # 110110_1_1111100

    # step 2 clear all bits to the right of p
    len_right = flipped.bit_length()-1-pos
    left = (flipped >> len_right << len_right)   # 1101101_0000000

    # step 3 add ones
    right = int((ones-1)*'1', 2)
    return (left | right) ^ mask if mask else left | right


def next_smaller(n):
    # step 1 flip last trailing zero to 1
    pos = last_trailing_zero(n)
    if pos is None:
        return
    flipped = n ^ flip_zero(n, pos)     # 110110011111_1_0

    # step 2 create mask with all 0 except 1 at position next(previous by index) to the last trailing zero
    mask = int('1', 2) << n.bit_length()-pos     # 00000000000_1_00
    # step 3 flipped XOR mask will clear the proper bit
    return flipped ^ mask


def smallest_and_largest(n):    # 11011001111100
    if n == 0:
        return
    larger = next_larger(n)
    smaller = next_smaller(n)
    print(larger, smaller)
    return bin(larger), smaller if smaller is None else bin(smaller)


if __name__ == '__main__':
    assert smallest_and_largest(int('11011001111100', 2)) == ('0b11011010001111', '0b11011001111010'), "('0b11011010001111', '0b11011001111010') Expected (13967, 13946)"
    assert smallest_and_largest(int('110110011', 2)) == ('0b110110101', '0b110101011'), "('0b110110101', '0b110101011') Expected (437, 427)"
    assert smallest_and_largest(int('110101111', 2)) == ('0b110110111', '0b110011111'), "('0b110110101', '0b110101011') Expected (439, 415)"
    assert smallest_and_largest(int('1111', 2)) == ('0b10111', None), "('0b110110101', '0b110101011') Expected (23, None)"

