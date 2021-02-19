# missing_number.py


"""
An array A contains all the integers from 0 to n, except for one number which is missing.
Cannot access an entire integer in A with a single operation.
The elements in A are represented in binary, and the only operation we can use to access them is "fetch the jth bit of A[i]"
"""


def missing_number(arr):
    switch, missing = '0', 0
    for i in range(len(arr)):
        if bin(arr[i])[-1] != switch:
            return missing
        switch = '1' if switch == '0' else '0'
        missing += 1
    return


if __name__ == '__main__':
    array = [i for i in range(100)]
    a1, a2, a3, a4, a5 = [list(array) for i in range(5)]
    a1.pop(0)
    a2.pop(1)
    a3.pop(56)
    a4.pop(98)
    a5.pop(99)
    assert missing_number(a1) == 0, f'Test 1 Failed, output is {missing_number(a1)} when 0 expected'
    assert missing_number(a2) == 1, f'Test 2 Failed, output is {missing_number(a2)} when 1 expected'
    assert missing_number(a3) == 56, f'Test 3 Failed, output is {missing_number(a3)} when 56 expected'
    assert missing_number(a4) == 98, f'Test 4 Failed, output is {missing_number(a4)} when 56 expected'
    assert missing_number(a5) is None, f'Test 4 Failed, output is {missing_number(a5)} when None expected'
