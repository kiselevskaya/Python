

import math


def dec2FactString(nb):
    extended_numbers = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    output = ''
    rest = nb
    # find the number, factorial of which is the closest to the given number
    max_factorial = 0
    while math.factorial(max_factorial) < nb:
        max_factorial += 1
    else:
        max_factorial -= 1
    # find the maximum multiplier for each factorial and add to output
    for number in range(max_factorial, -1, -1):
        subtractions = []
        for multiplier in range(0, number+1):
            if rest - multiplier*math.factorial(number) >= 0:
                subtractions.append(rest - multiplier*math.factorial(number))
        rest = min(subtractions)
        output += extended_numbers[subtractions.index(min(subtractions))]
        subtractions = []
    return output


def factString2Dec(string):
    extended_numbers = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    output, number = 0, 0
    for multiplier in list(string)[::-1]:
        multiplier = extended_numbers.index(multiplier)
        output += multiplier*math.factorial(number)
        number += 1
    return output


print(factString2Dec("341010"))
print(dec2FactString(463))
