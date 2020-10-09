fn = raw_input("Enter a file name:")
try:
    fh = open(fn)
except:
    print "File cannot be opened"
count = 0
for line in fh:
    line = line.rstrip()
    count = count + 1
    if count < 6:
        print line
