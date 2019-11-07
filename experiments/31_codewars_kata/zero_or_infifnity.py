

import math
import re
from decimal import *


def going(n):
    # multiplier = sum([math.factorial(x) for x in range(n, 0, -1)])
    # if n < 170:
    #     full_number = 1/math.factorial(n)*multiplier
    # else:
    #     full_number = (Decimal(1)/math.factorial(n))*multiplier
    #     print(full_number)
    # output = float(re.search(r'\d+\.\d{0,6}', str(full_number))[0])
    # return output

    # s = 0
    # f = 1
    # for i in range(1, n+1):
    #     f = f*i
    #     s += f
    # output = Decimal(int((Decimal(s)/f)*1000000))/1000000

    x = Decimal(1)
    s = Decimal(0)
    while n > 0 and x > 0.00000000001:
        s += x
        x /= n
        n -= 1
    output = float(Decimal(int(s*1000000))/1000000)
    return output


print(going(200))
