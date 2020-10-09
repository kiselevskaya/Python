import xml.etree.ElementTree as ET
import urllib

numlist = list()

while True:
    input = raw_input("Enter location: ")
    if len(input) < 1: break

    print 'Retrieving ', input
    uh = urllib.urlopen(input)
    data = uh.read()
    print 'Retrieved ',len(data),'characters'

    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    print 'Count:', len(lst)

    for item in lst:
        num = item.find('count').text
        num = int(num)
        numlist.append(num)

    print "Sum: ", sum(numlist)
    quit()

#http://python-data.dr-chuck.net/comments_42.xml
#2553
#http://python-data.dr-chuck.net/comments_249469.xml
#2325
