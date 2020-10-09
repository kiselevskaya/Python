try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print 'Error, please enter numeric input'
    quit()
# print pay
if h <= 40:
    pay = h * r
else:
    pay = 40 * r + (h - 40) * (1.5 * r)
print pay
