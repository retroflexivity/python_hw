mapping = {'nom': 'им', 'gen': 'род', 'dat': 'дат', 'acc': 'вин', 'ins': 'тв', 'instr': 'тв', 'prep': 'предл'}
newfile = ''

filename = input('Введите полное имя файла\n')

with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        starti = line.find('Case=') + 5
        if starti > 4:
            endi = starti
            for ch in line[starti:]:
                if not ch.isalpha():
                    break
                endi += 1
            latincase = line[starti:endi].lower()
            if latincase in mapping:
                line = line[:starti] + mapping[latincase] + line[endi:]

        newfile += line

with open(filename, 'w', encoding='utf-8') as file:
    file.write(newfile)
