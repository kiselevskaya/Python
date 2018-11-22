

code = ',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.'

open_brackets = []
brackets = {}

for i in range(len(code)):
    if code[i] == '[':
        open_brackets.append(i)
    elif code[i] == ']':
        brackets[i] = open_brackets[-1]
        open_brackets.pop()

now = 24


print(brackets)
print(brackets[now])

