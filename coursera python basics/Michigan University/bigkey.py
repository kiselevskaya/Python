fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "File cannot be opened", fname
    quit()

lst = list()
for line in fh:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == "From:":
        words = words[1]
        lst.append(words)

counts = dict()
for element in lst:
    counts[element] = counts.get(element, 0) + 1
#print counts

bigkey = None
bigcount = None
for key in counts:
    if bigcount is None or counts[key] > bigcount:
        bigkey = key
        bigcount = counts[key]
print bigkey, bigcount
