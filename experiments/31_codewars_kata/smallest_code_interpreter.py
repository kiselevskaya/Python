

def brain_luck(code, input):
    input_lst = decode_utf(input)
    code_index, input_index, work_on, i = 0, 0, 0, 0
    output, open_brackets, close_brackets, data = [], [], [], []

    while code_index < len(code):
        if code[code_index] == ',':
            work_on = input_lst[input_index]
            input_index += 1
        elif code[code_index] == '.':
            output.append(work_on)
        elif code[code_index] == '+':
            if work_on == 255:
                work_on = 0
            else:
                work_on += 1
        elif code[code_index] == '-':
            if work_on == 0:
                work_on = 255
            else:
                work_on -= 1

        elif code[code_index] == '<':
            if len(data) == 0:
                data.append(work_on)
            else:
                data[i] = work_on
            if i == 0:
                work_on = 0
            else:
                work_on = data[i-1]
                i -= 1

        elif code[code_index] == '>':
            if len(data) == 0:
                data.append(work_on)
            else:
                data[i] = work_on
            if i == len(data)-1:
                data.append(0)
            i += 1
            work_on = data[i]

        elif code[code_index] == '[':
            if code_index not in open_brackets:
                open_brackets.insert(0, code_index)
            elif work_on == 0:
                while code[code_index] != ']':
                    code_index += 1

        elif code[code_index] == ']':
            if code_index not in close_brackets:
                close_brackets.insert(0, code_index)
            if work_on != 0:
                code_index = open_brackets[close_brackets.index(code_index)]
            if work_on == 0:
                open_brackets.pop(0)
                close_brackets.pop(0)

        code_index += 1

    output = ''.join([chr(n) for n in output])
    return output


def decode_utf(input):
    out = []
    for i in input.split(", "):
        try:
            j = i.encode('utf-8').decode('utf-8', 'replace')
        except Exception as e:
            # print(e)
            j = i.decode('utf-8', 'replace')
        try:
            out.append(int(j))
        except Exception as e:
            # print(e)
            out.append([ord(l) for l in list(j)])
    flat_list = []
    _ = [flat_list.extend(item) if isinstance(item, list) else flat_list.append(item) for item in out if item]

    return flat_list


print(brain_luck('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.', ''))
print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)))    # 'Codewars'
print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))   # chr(72)

# print(brain_luck(',+[-.,+]', tk + chr(255)))
# print(brain_luck(<None given>, '11, 11, 2(, 3\x1f, 5\r, 8\xf2, =\xc5, E}, R\x08, gK, '))  # '1, 1, 2, 3, 5, 8, 13, 21, 34, 55'
# check = '11, 11, 2(, 3\x1f, 5\r, 8\xf2, =\xc5, E}, R\x08, gK, '
# print(decode_utf(check))
