import re
name = open("regex_sum_249467.txt")
text = name.read()
lst = re.findall("[0-9]+", text)
numlist = list()
for num in lst:
    num = int(num)
    numlist.append(num)
print sum(numlist)
#print sum(int(lst))
#print sum([ ****** *** * in **********('[0-9]+',**************************.read("regex_sum_42.txt")) ])
