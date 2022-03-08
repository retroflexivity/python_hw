from os import walk

path, f = input('Введите папку и файл через пробел\n').split()

unfound = True
for dir in walk(path):
    if f in dir[2]:
        print('да')
        unfound = False
        break

if unfound:
    print('нет')
