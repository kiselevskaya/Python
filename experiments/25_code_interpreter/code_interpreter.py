

# brain_luck(',[.[-],]', 'Codewars' + chr(0)), 'Codewars')


def brain_luck(code, input):
    output = []
    index_code = 0
    index_input = 0
    array = [ord(l) for l in list(input)]
    work_on = 0
    data = [0]
    data_index = 0

    open_brackets = []
    brackets = {}

    for i in range(len(code)):
        if code[i] == '[':
            open_brackets.append(i)
        elif code[i] == ']':
            brackets[i] = open_brackets[-1]
            open_brackets.pop()

    while index_code < len(code):
        data[data_index] = work_on
        if code[index_code] == ',':
            work_on = array[index_input]
            index_input += 1
        elif code[index_code] == '.':
            output.append(work_on)
        elif code[index_code] == '+':
            work_on += 1
        elif code[index_code] == '-':
            work_on -= 1
        elif code[index_code] == '<':
            data_index -= 1
            work_on = data[data_index]
        elif code[index_code] == '>':
            data_index += 1
            try:
                work_on = data[data_index]
            except IndexError:
                work_on = 0
                data.append(work_on)
        elif code[index_code] == '[':
            if work_on == 0:
                while code[index_code] != ']':
                    index_code += 1

        elif code[index_code] == ']':
            if work_on != 0:
                index_code = brackets[index_code]
 
        index_code += 1

    output = ''.join([chr(n) for n in output])
    return output


print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))
