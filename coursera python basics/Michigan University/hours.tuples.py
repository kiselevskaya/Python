fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "File cannot be opened", fname
    quit()
lst = list()
for line in fh:
    words = line.rstrip().split()
    if len(words) == 0 : continue
    if words[0] == "From":
        words = words[5].split(":")
        words = words[0]
        lst.append(words)
counts = dict()
for word in lst:
    counts[word] = counts.get(word, 0) + 1
new = list()
for key, value in counts.items():
    new.append( (key, value) )
new.sort(reverse = True)
new.reverse()
for key,value in new[:]:
    print key, value
