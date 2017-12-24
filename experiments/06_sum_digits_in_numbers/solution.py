
import string
import re

numbers = open('../00_text_files/out.txt', 'rt')
new_file = open('../00_text_files/out2.txt', 'w+')

sum_nums = []
for line in numbers.readlines():
    n = line.rstrip('\n')
    s = 0
    for d in n:
        s += int(d)
    new_file.write(str(s))
    new_file.write('\n')
    sum_nums.append(s)

print(sum_nums)
