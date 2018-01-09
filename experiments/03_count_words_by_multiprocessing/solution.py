# -*- coding: utf-8 -*-
import threading
import string
import re
import time
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

def calculon(text, word):
    result = 0
    for item in text:
        if item == word:
            result += 1
    return result

q = JoinableQueue()
ans = JoinableQueue()

for word in words:
    q.put(word)

def full_calc(text, q, ans):
    while True:
        word = q.get()
        if word is None:
            break
        count = calculon(text, word)
        ans.put([word, count])
        q.task_done()

thread_count = 8
threads = []
for i in range(thread_count):
    thread = Process(target=full_calc, args=(text, q, ans))
    threads.append(thread)
    thread.start()

q.join()

for i in range(thread_count):
    q.put(None)

for thread in threads:
    thread.join()

while not ans.empty():
    print(ans.get())
