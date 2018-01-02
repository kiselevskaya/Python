import time
import re
import string
import math

start = time.time()
start_time = time.time()

file = open('../00_text_files/war-and-peace-I.txt', 'rt')
content = file.read()
file.close()
print ('{} sec'.format(time.time() - start_time))
start_time = time.time()

start_process = time.time()
text = content.split()
new_text = []
for word in text:
    word = re.sub('['+string.punctuation+']', '', word).replace('–', '').replace('«', '').replace('»', '').replace('…', '').lower()
    if word != "":
        new_text.append(word)
text = new_text
print ('{} sec'.format(time.time() - start_time))
start_time = time.time()

length = []
for word in text:
    length.append(len(word))
print ('{} sec'.format(time.time() - start_time))
start_time = time.time()

sort = sorted(length)
print ('{} sec'.format(time.time() - start_time))
start_time = time.time()

medium = sum(sort)/len(sort)
count_I = 0
count_II = 0
for word in text:
    if len(word) < medium:
        count_I += 1
    elif len(word) > medium:
        count_II += 1
print ('{} sec'.format(time.time() - start_time))
start_time = time.time()

if count_I > count_II:
    print('More words with length less than medium: {} > {}'.format(count_I, count_II))
else:
    print('More words with length more than medium: {} > {}'.format(count_II, count_I))

#process time
print ('{} sec for all.'.format(time.time() - start))
