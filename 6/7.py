operands = ['+', '-', '=', '!', '>', '<']
ok = True

with open(input('Введите название файла\n'), encoding='UTF_8') as text:  # в этой конкретной строке рер8 с нами не согласен
    for i in range(len(code := text.readlines())):
        for j in range(len(line := code[i])):
            if line[j] in operands:
                if not((line[j - 1] == ' ' or (line[j - 1] in (operands + [':']) and line[j - 2] == ' ')) and (line[j + 1] == ' ' or (line[j + 1] in operands and line[j + 2] == ' '))):
                    print('Строчка', i + 1, ' — некрасивая')
                    ok = False
                    break

if ok:
    print('Ок')
