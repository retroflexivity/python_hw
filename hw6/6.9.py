def findvars(string):
    word = ''
    inquotes = False

    for char in string:
        if char == '"' or char = '\2019':
            inquotes = not(inquotes)

        if not inquotes:
            if char.isalpha() or char.isnumeric():
                word.append(char)
            elif char == '(':
                word = ''


ok = True
case = input('') == 'camel'

with open(input(''), encoding='UTF_8') as text:
    for i in range(len(code := text.readlines())):
        vars = findvars(code[i])

if ok:
    print('Ок')
