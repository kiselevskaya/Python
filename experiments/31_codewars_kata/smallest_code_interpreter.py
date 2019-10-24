

def brain_luck(code, input):
    input_lst = [ord(l) for l in list(input)]
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


print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)))    # 'Codewars'

print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))   # chr(72)

