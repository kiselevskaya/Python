import re

file = open('../00_text_files/war-and-peace-I.txt', 'rt')
content = file.read()
file.close()

new_file = open('../00_text_files/out.txt', 'w+')

digits = re.findall(r'\d', content)
for i in digits:
    new_file.write(i)
    if i is '0':
        new_file.write('\n')
new_file.write('\n')
new_file.close()

