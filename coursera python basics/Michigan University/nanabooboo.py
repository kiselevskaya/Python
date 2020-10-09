fn = raw_input("Enter a file name:")
if fn == "na na boo boo":
    print "NA NA BOO BOO TO YOU - You have been punk'd!"
    quit()
try:
    fh = open(fn)
except:
    print "File cannot be opened"
    quit()
count = 0
for line in fh:
    line = line.rstrip()
    count = count + 1
print "There were %d subject lines in %s" % (count, fn)
