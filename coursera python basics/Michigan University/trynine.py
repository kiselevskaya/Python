# try nine
hrs = raw_input('Enter Hours integer:\n')
try:
    h = int(hrs)
except:
    print 'Error, please enter numeric input'
    quit()
rate = raw_input('Enter Rate integer:\n')
try:
    r = int(rate)
except:
    print 'Error, please enter numeric input'
    quit()
pay = h * r
print pay
