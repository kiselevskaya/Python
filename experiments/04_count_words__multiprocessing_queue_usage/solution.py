import string
import re
import time
import math
from multiprocessing import Process, JoinableQueue

file = open('../00_text_files/war-and-peace-I.txt', 'rt')
content = file.read()
file.close()

text = content.split()
new_text = []
for word in text:
    word = re.sub('['+string.punctuation+']', '', word).replace('–', '').replace('«', '').replace('»', '').replace('…', '').lower()
    if word != "":
        new_text.append(word)
text = new_text

words = ['я', 'ты', 'дети', 'а', 'от', 'к', 'до', 'по', 'с', 'ты', 'дети', 'а', 'от', 'к', 'до', 'по', 'с']
process_count = 8
q_text= JoinableQueue()
ans = JoinableQueue()

def group(i, text, parts, q):
    ending = i * math.ceil(len(text) / parts)
    opening = (i - 1) * math.ceil(len(text) / parts)
    if ending >= (len(text) - 1):
        ending = len(text)
    else:
        ending = ending - 1
    # print("{} {}".format(opening, ending))
    part = text[opening:ending]
    return part

print(len(text))

for i in range(process_count):
    q_text.put(group(i + 1, text, process_count, q_text))

def calculon(text_part, words):
    dictionary = {}
    for item in text_part:
        for word in words:
            if item == word:
                if word not in dictionary:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
    return dictionary

def full_calc(words, q, ans):
    while True:
        text_part = q.get()
        if text_part is None:
            break
        dictionary = calculon(text_part, words)
        ans.put(dictionary)
        q.task_done()

processes = []
for i in range(process_count):
    process = Process(target=full_calc, args=(words, q_text, ans))
    processes.append(process)
    process.start()

q_text.join

for i in range(process_count):
    q_text.put(None)

for process in processes:
    process.join()

final_ans = {}
while not ans.empty():
    dictionary = ans.get()
    for word, count in dictionary.items():
        if word not in final_ans:
            final_ans[word] = count
        else:
            final_ans[word] += count

print(final_ans)
