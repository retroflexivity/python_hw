from os import mkdir
from shutil import rmtree
from os.path import isdir

error = 'ошибка существования'

while True:
    cmd = input('что вы хотите сделать\n').split()
    if cmd[0] == 'создай':
        if not isdir(cmd[1]):
            mkdir(cmd[1])
        else:
            print(error)
    elif cmd[0] == 'удали':
        if isdir(cmd[1]):
            rmtree(cmd[1])
        else:
            print(error)
    elif cmd[0] == 'надоело':
        break
    else:
        print('я так не умею')
