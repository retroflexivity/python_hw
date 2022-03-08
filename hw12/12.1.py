from os import listdir
from os.path import isfile, join, splitext
from collections import Counter


def getfiles(path):
    files = [(splitext(f)) for f in listdir(path) if isfile(join(path, f))]
    cnt = Counter([f[1] for f in files])
    for ext in cnt:
        print(ext, cnt[ext])
        for f in sorted(files):
            if f[1] == ext:
                print('  ' + f[0] + f[1])
    return


getfiles('/home/retroflexivity/python_hw/hw11')
