from os import listdir
from os.path import isfile, join, splitext
from collections import Counter

path = input('Введите путь\n')
files = [splitext(f) for f in listdir(path) if isfile(join(path, f))]

cnt = Counter([f[0] for f in files])
for i in cnt:
    if cnt[i] > 1:
        print(i)
        for f in files:
            if f[0] == i:
                print('  ' + f[0] + f[1])
