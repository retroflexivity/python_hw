def findvars(string):
    keywords = ['False', 'def', 'if', 'raise', 'None', 'del', 'import', 'return', 'True', 'elif', 'in', 'try', 'and', 'else', 'is', 'while', 'as', 'except', 'lambda', 'with', 'assert', 'finally', 'nonlocal', 'yield', 'break', 'for', 'not', 'class', 'from', 'or', 'continue', 'global', 'pass']  # https://realpython.com/lessons/reserved-keywords/

    vars = []
    word = ''
    inquotes = False

    for char in string:
        if char == '"' or char == "'":
            inquotes = not(inquotes)

        if not inquotes:
            if char == '#':
                continue
            if char.isalpha() or char.isnumeric():
                word += char
            elif char == '(':  # функция. не переменная
                word = ''
            else:
                if word and (word not in keywords):
                    vars.append(word)
                word = ''
    return(vars)


ok = True
camel = input('Введите стиль написания\n') == 'camel'

with open(input('Введите название файла\n'), encoding='UTF_8') as text:
    for i in range(len(code := text.readlines())):
        vars = findvars(code[i])
        if camel:
            for var in vars:
                if var[0].islower() or '_' in var:
                    print(i + 1)
                    ok = False
                    break
        else:
            for var in vars:
                for char in var:
                    if char.isupper():
                        print(i + 1)
                        ok = False
                        break
                if not ok:
                    break
        if not ok:
            break


if ok:
    print('Ок')
