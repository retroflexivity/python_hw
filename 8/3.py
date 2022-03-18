from random import sample

filename = input('Введите полное имя файла\n')

with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

n = int(input('Введите количество строк\n'))
smp = sample(lines, n)
for i in smp:
    print(i[:-1])
