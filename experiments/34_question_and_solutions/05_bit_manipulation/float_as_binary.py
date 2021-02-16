# float_as_binary.py


"""
Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double, print the binary representation.
If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".

For Integer Part, keep dividing the number by 2 and noting down the remainder until and unless the dividend is less than 2.
If so, stop and copy all the remainders together.
For Decimal Part, keep multiplying the decimal part with 2 until and unless 0 left as fractional part.
After multiplying the first time, note down integral part and again multiply decimal part of the new value by 2.
Keep doing this until reached a perfect number.
"""


def float_as_binary(n):
    if n < 0 or n > 1:
        return 'Input Error'
    output = '.'
    while n:
        if len(output) >= 32:
            return 'ERROR'
        i, n = 0, n*2
        if n >= 1:
            i, n = 1, n-1
        output += str(i)
    return output


if __name__ == '__main__':
    num = 0.72
    assert float_as_binary(num) == 'ERROR', 'Test1: ERROR Expected as binary of 0.72 is .1011100001010001111010111000010(1011100001010001111010111000010)'
    # 0.72*2 = (1).44*2 = (0).88*2 = (1).76*2 = (1).52*2 = (1).04*2 = (0).08*2 = (0).16*2 = (0).32*2 = (0).64*2 =
    # = (1).28*2 = (0).56*2 = (1).12*2 = (0).24*2 = (0).48*2 = (0).96*2 = (1).92*2 = (1).84*2 = (1).68*2 = (1).36*2 = (0).72

    num2 = 0.5
    assert float_as_binary(num2) == '.1', 'Test2: No Error Expected as output is 2 characters long'

    num3 = 0.06909999996423721
    assert float_as_binary(num3) == '.000100011011000010001001101', 'Test3: No Error Expected as output is 28 characters long'

    num4 = 0.6011999999172986
    assert float_as_binary(num4) == '.1001100111101000001111100100001', 'Test4: No Error Expected as output is 32 characters long'

    num5 = 1.1
    assert float_as_binary(num5) == 'Input Error', 'Test5: Input number should be not negative float between 0 and 1'

    num6 = -0.1
    assert float_as_binary(num6) == 'Input Error', 'Test6: Input number should be not negative float between 0 and 1'

    num7 = 0.10490000038407743
    assert float_as_binary(num7) == 'ERROR', 'Test7: ERROR Expected as binary for 0.10490000038407743 is 33 characters long'

