from os import listdir
from os.path import isfile, join, getsize

path = input('Введите путь\n')
files = [f for f in listdir(path) if isfile(join(path, f))]
for f in sorted(files):
    print(f, getsize(join(path, f)))
