import random as r


def rps(usr):
    words = ['rock', 'paper', 'scissors']
    comp = r.choice([0, 1, 2])
    print(words[comp])
    usr = words.index(usr)
    if (comp - usr == 0):
        return('draw')
    elif (comp - usr == 1) or (comp - usr == -2):
        return('lose')
    else:
        return('win')


rps('rock')
