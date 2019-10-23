

def josephus(items, k):
    result, index_lst, count = [], [], 0
    while len(items) > 0:
        for i in range(len(items)):
            count += 1
            if count == k:
                result.append(items[i])
                index_lst.append(i)
                count = 0
        rest = []
        for i in range(len(items)):
            if i not in index_lst:
                rest.append(items[i])
        items, index_lst = rest, []

        print('result: ', result, ' rest: ', items)
    return result


print(josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4))    # ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']


# Best solution!
# def josephus(xs, k):
#     i, ys = 0, []
#     while len(xs) > 0:
#         i = (i + k - 1) % len(xs)
#         ys.append(xs.pop(i))
#     return ys




