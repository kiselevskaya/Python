# add_operator_only.py


def multiply(a, b):
    # Check that Input is correct, both numbers are integers
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Invalid input'
    if a == 0 or b == 0:
        return 0
    count, result = 0, 0
    # Add <a> to result <b> times (or <b> <a> times)
    while count < abs(b):
        result += abs(a)
        count += 1
    if a < 0 < b or b < 0 < a:
        return int(f'-{result}')
    return result


def subtract(a, b):
    # Check that Input is correct, both numbers are integers
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Invalid input'
    # Minuend equal to 0
    if a == 0:
        # Returns negative of absolute value of subtrahend if <b> is positive and absolute value if <b> is negative
        return int(f'-{b}') if b > 0 else abs(b)
    # Returns minuend if subtrahend equal to 0
    if b == 0:
        return a
    # If minuend is negative and subtrahend is positive, difference will be negative sum of their absolut values
    if a < 0 < b:
        return int(f'-{abs(a)+b}')
    # Negative minuend minus negative subtrahend is same as absolut value of subtrahend minus absolut value of minuend
    if a < 0 and b < 0:
        return subtract(abs(b), abs(a))
    # Subtract negative subtrahend is same as add it absolut value
    if a > 0 > b:
        return a+abs(b)
    result = 0
    # Finds the difference by adding ones to min of minuend and subtrahend to rich max of their
    m, n = (a, b) if a > b else (b, a)
    while n < m:
        result += 1
        n += 1
    # Return negative result if absolut value of subtrahend was larger
    return result if a > b else int(f'-{result}')


def divide(a, b):
    result = 0
    # By subtracting ones at a time divisor from dividend adds 1 to result
    while a >= b:
        a = subtract(a, b)
        result += 1
    # Returns quotient and remainder
    return result, a


def divide_with_fraction(a, b):
    # Check that Input is correct, both numbers are integers
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Invalid input'
    # Dividend equal to 0
    if a == 0:
        return 0
    # Division by zero
    if b == 0:
        return
    # Whole part and remainder
    result, remainder = divide(abs(a), abs(b))
    # Finds fraction of maximum length <5> if division without remainder is not possible
    fraction = ''
    if remainder > 0:
        while remainder > 0 or len(fraction) < 5:
            output = divide(int(f'{remainder}0'), abs(b))
            fraction, remainder = f"{fraction}{output[0]}", output[1]
    # If division without remainder is not possible return result as float number
    result = float(f'{result}.{fraction}') if bool(fraction) else result
    # If one dividend or divisor is negative result would be negative
    if a < 0 < b or b < 0 < a:
        result = int(f'-{result}')
    return result


if __name__ == '__main__':
    assert multiply(3, 0) == 0, 'MultiplyTest 1 3*0=0'
    assert multiply(0, 3) == 0, 'MultiplyTest 2 0*3=0'
    assert multiply(3, 4) == 12, 'MultiplyTest 3 3*4=12'
    assert multiply(-3, 4) == -12, 'MultiplyTest 4 -3*4=-12'
    assert multiply(3, -4) == -12, 'MultiplyTest 5 3*(-4)=-12'
    assert multiply(-5, -3) == 15, 'MultiplyTest 6 -5*(-3)=15'
    assert multiply(-5, 3.0) == 'Invalid input', 'Test 7 <b> is float'
    assert multiply('5', 3) == 'Invalid input', 'Test 8 <a> is string'

    assert subtract(3, 0) == 3, 'SubtractTest 1 3-0=3'
    assert subtract(0, 3) == -3, 'SubtractTest 2 0-3=-3'
    assert subtract(3, 4) == -1, 'SubtractTest 3 3-4=-1'
    assert subtract(-3, 4) == -7, 'SubtractTest 4 -3-4=-7'
    assert subtract(3, -4) == 7, 'SubtractTest 5 3+4=7'
    assert subtract(-5, -3) == -2, 'SubtractTest 6 -5+3= 3-5= -2'

    assert divide_with_fraction(3, 0) is None, 'DivideWithFractionTest 1 3/0 is None'
    assert divide_with_fraction(0, 3) == 0, 'DivideWithFractionTest 2 0-3=-0'
    assert divide_with_fraction(6, 3) == 2, 'DivideWithFractionTest 3 6/3=2'
    assert divide_with_fraction(5, 2) == 2.5, 'DivideWithFractionTest 4 5/2=2.5'
    assert divide_with_fraction(-12, 3) == -4, 'DivideWithFractionTest 5 -12/3=-4'
    assert divide_with_fraction(12, -4) == -3, 'DivideWithFractionTest 6 12/(-4)=-3'
    assert divide_with_fraction(-15, -3) == 5, 'DivideWithFractionTest 7 -15/(-3)=5'

