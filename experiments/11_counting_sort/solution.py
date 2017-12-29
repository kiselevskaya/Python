lst = [4, 7, 0, 4, 4, 4, 2, 6, 9, 1, 4, 100]
#lst = [3, 6, 8, 13, 2, 5]
count = []

ln = max(lst) + 1
for i in range(ln):
    count.append(0)

#print (count)
# count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for e in range(len(lst)):
    count[lst[e]] += 1
#print (count)
# count = [1, 1, 1, 0, 2, 0, 1, 1, 0, 1]
b = 0
for j in range(ln):
    for i in range(count[j]):
        count[j] -= 1
        lst[b] = j
        b += 1

print (lst)
