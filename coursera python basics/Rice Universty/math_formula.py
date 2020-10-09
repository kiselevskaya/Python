import math
def math_formula(x):
    math_formula = -5 * (x ** 5) + 69 * (x ** 2) -47
    return math_formula
results = []
for value in range(0, 4):
    print 'For f(',(value),')', 'the number is:' , math_formula(value)
    results.append(math_formula(value))

print max(results)
