fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print "File cannot be opened", fname
    quit()

count = 0
for line in fh:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == "From:":
        print words[2]
        count = count + 1
    else: continue
print "There were", count, "lines in the file with From as the first word"
