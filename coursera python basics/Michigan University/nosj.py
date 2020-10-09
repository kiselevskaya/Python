import urllib
import json

numlist = list()

while True:
    input = raw_input("Enter location: ")
    if len(input) < 1: break

    print 'Retrieving ', input
    uh = urllib.urlopen(input)
    data = uh.read()
    print 'Retrieved ',len(data),'characters'
    #print data

    tree = json.loads(data)
    lst = tree["comments"]
    print 'Count:', len(lst)

    for item in lst:
        num = item["count"]
        num = int(num)
        numlist.append(num)

    print "Sum: ", sum(numlist)
    quit()

#http://python-data.dr-chuck.net/comments_42.json
#2553
#http://python-data.dr-chuck.net/comments_249473.json
#25
