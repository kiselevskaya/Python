import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

count = 0
numlist = list()
tags = soup('span')
for tag in tags:
    num = tag.contents[0]
    num = int(num)
    numlist.append(num)
    count = count + 1
print count
print sum(numlist)
