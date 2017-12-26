import operator
import string
import re
import time

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

words = ['я', 'ты', 'дети', 'а', 'от', 'к', 'до', 'по', 'с']
def calculon(text, words):
    dictionary = {}
    for item in text:
        for word in words:
            if item == word:
                if word not in dictionary:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
    return dictionary

dct = calculon(text, words)
dct_sort = sorted(dct.items(),key = operator.itemgetter(1))
print (dct_sort)
