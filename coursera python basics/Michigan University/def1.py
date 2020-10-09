def computepay(h,r):
        if h <= 40:
            pay = h * r
        else:
            pay = 40 * r + (1.5 * r * (h - 40))
        return pay
try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print 'Error, please enter numeric input'
    quit()
p = computepay(h,r)
print p
