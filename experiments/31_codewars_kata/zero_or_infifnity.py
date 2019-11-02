

import math
import re


def going(n):
    multiplier = sum([math.factorial(x) for x in range(n, 0, -1)])
    full_number = 1/math.factorial(n)*multiplier
    output = float(re.findall(r'\d+\.\d{0,6}', str(full_number))[0])
    return output


print(going(5))
