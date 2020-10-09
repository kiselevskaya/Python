fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "File cannot be opened", fname
    quit()
lst = list()
for line in fh:
    words = line.rstrip().split()
    lst.extend(words)

new = list()
for x in sorted(set(lst)):
    new.append(x)
print new
