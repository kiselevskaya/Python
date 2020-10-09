import re
import urllib
from BeautifulSoup import *

count = raw_input("Enter count ")
c = int(count)
position = raw_input("Enter position ")
p = int(position)

url = raw_input("Enter URL ")
pages = list()
pages.append(url)
newlst = list()
newlst.append(url)

while True:
    if len(newlst) != c + 1:
        for page in pages:
            html = urllib.urlopen(page).read()
            soup = BeautifulSoup(html)
            tags = soup('a')
            tgs = []
            for tag in tags:
                tgs.append(tag.get("href", None))
                if len(list(tgs)) != p: continue
                else:
                    new = tgs[p - 1]
                    newlst.append(new)
                    pages.append(new)
                    del pages[:-1]
    else:
        #print newlst
        name = newlst[-1]
        name = re.findall("_by_(.+).html", name)
        print name
        quit()

#http://python-data.dr-chuck.net/known_by_Fikret.html
#Fikret Montgomery Mhairade Butchi Anayah

#http://python-data.dr-chuck.net/known_by_Babyjane.html
#startwith(R)
