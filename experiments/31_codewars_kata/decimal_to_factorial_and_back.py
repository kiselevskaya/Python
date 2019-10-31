

import math


def dec2FactString(nb):
    output = ''
    rest = nb
    # find the number, factorial of which is the closest to the given number
    max_factorial = 0
    while math.factorial(max_factorial) < nb:
        max_factorial += 1
    else:
        max_factorial -= 1
        print('factorial ', max_factorial, ' is ', math.factorial(max_factorial))
    # find the maximum multiplier for each factorial and add to output
    for factor in range(max_factorial, 0, -1):
        subtractions = []
        for multiplier in range(0, factor+1):
            if rest - multiplier*math.factorial(factor) >= 0:
                subtractions.append(rest - multiplier*math.factorial(factor))
        rest = min(subtractions)
        output += str(subtractions.index(min(subtractions)))
        subtractions = []

    return output


def factString2Dec(string):
    number, n = 0, 0
    for i in list(string)[::-1]:
        number += int(i)*math.factorial(n)
        n += 1
    return number


# print(factString2Dec("341010"))
print(dec2FactString(463))
# test.assert_equals(dec2FactString(463), "341010")
# test.assert_equals(factString2Dec("341010"), 463)
