fn = raw_input("Enter a file name:")
try:
    fh = open(fn)
except:
    print "File cannot be opened"

count = 0
sum = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        x = line.find(" ")
        line = line[x + 1:]
        num = float(line)
        sum = sum + num
print "Average spam confidence:", sum/count
