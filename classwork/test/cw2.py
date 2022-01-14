def isnoun(entry, gender):
    sep1 = entry.find('|')
    sep2 = entry.find('|', sep1 + 1)

    grammar = entry[sep1 + 1:sep2].split()
    if grammar[0] == 'сущ':
        if ('ед' in grammar):
            if (gender in grammar):
                return(entry[:sep1], float(entry[sep2 + 1:]))
    return('', 0)


max = 0
gender = input('Укажите род: "муж", "ср" или "жен" (по умолчанию женский)\n')
minipm = input('Укажите граничное значение частоты на миллион (по умолчанию 100)\n')
if not gender:
    gender = 'жен'
if not minipm:
    minipm = 100
else:
    minipm = int(minipm)

with open('freqdict.ru.txt', encoding='utf-8') as dict:
    with open('freqdict_out.txt', 'w', encoding='utf-8') as out:

        for line in dict:
            noun, ipm = isnoun(line, gender)
            if noun and (ipm > minipm):
                out.write(noun + '\n')
                if ipm > max:
                    max = ipm
print('Максимальная частота: ', max, 'на миллион')
