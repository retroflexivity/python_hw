from os import listdir
from os.path import isfile, join, splitext


def getfiles(path):
    files = [(splitext(f)[1], splitext(f)[0]) for f in listdir(path) if isfile(join(path, f))]
    ext = ''
    for tup in sorted(set(files)):
        if tup[0] != ext:
            print(tup[0])
            ext = tup[0]
        print('  ' + tup[1] + tup[0])

    return


print(getfiles('/home/retroflexivity/python_hw/hw11'))
