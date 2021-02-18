# same_one_bits.py


"""
Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.
"""


def non_trailing(n, v):
    a, b = ('1', '0') if v == 1 else ('0', '1')
    n = bin(n)[2:]
    count = 0
    zero = False
    for i in range(len(n)-1, -1, -1):
        if n[i] == '1':
            count += 1
        if n[i] == a and not zero:
            zero = True
        if zero and n[i] == b:
            return i, count
    return None, count


def flip_zero(n, p):
    left = int(p*'1', 2) << n.bit_length()-p
    right = int(n.bit_length()*'1', 2) >> p+1
    mask = (int(n.bit_length()*'1', 2)) ^ (left | right)
    return mask


def next_larger(n):
    mask = False
    # step 1 flip non-trailing 0 to 1
    pos, ones = non_trailing(n, 1)
    # if all bits are 1
    if pos is None:
        mask = int('1', 2) << n.bit_length()+1
        n = mask | n
        pos, ones = non_trailing(n, 1)
    flipped = n ^ flip_zero(n, pos)

    # step 2 clear all bits to the right of p
    len_right = flipped.bit_length()-1-pos
    left = (flipped >> len_right << len_right)

    # step 3 add ones
    right = int((ones-1)*'1', 2)
    return (left | right) ^ mask if mask else left | right


def next_smaller(n):
    # step 1 flip all bits starting from the last non-trailing 1 to 0
    pos, ones = non_trailing(n, 0)
    if pos is None:
        return
    n = (int((pos+1)*'1', 2) << n.bit_length()-pos) & n

    # step 2 create mask for the right amount of ones (starting from next to the non-trailing 1 position) followed by zeros
    mask = int(ones*'1', 2) << (n.bit_length()-pos-1-ones)
    return n | mask


def smallest_and_largest(n):
    if n == 0:
        return
    larger = next_larger(n)
    smaller = next_smaller(n)
    return bin(larger), smaller if smaller is None else bin(smaller)


if __name__ == '__main__':
    assert smallest_and_largest(int('11011001111100', 2)) == ('0b11011010001111', '0b11011001111010'), "('0b11011010001111', '0b11011001111010') Expected (13967, 13946)"
    assert smallest_and_largest(int('110110011', 2)) == ('0b110110101', '0b110101110'), "('0b110110101', '0b110101011') Expected (437, 430)"
    assert smallest_and_largest(int('110101111', 2)) == ('0b110110111', '0b110011111'), "('0b110110101', '0b110101011') Expected (439, 415)"
    assert smallest_and_largest(int('1111', 2)) == ('0b10111', None), "('0b110110101', '0b110101011') Expected (23, None)"
