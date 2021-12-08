ok = True

with open(input(''), encoding='UTF_8') as text:
    for i in range(len(code := text.readlines())):
        if (length := len(code[i])) > 79:
            print('Строчка', i + 1, '— слишком длинная, в ней', length, 'символов')
            ok = False
            break
if ok:
    print('Ок')
