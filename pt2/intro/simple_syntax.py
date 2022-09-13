from random import choice, randint


def get_np(det, n, pl):
    if pl and (det == 'a'):
        det = ''
    return det + ' ' * bool(det) + n + 's' * pl


def get_vp(v, time, pl):
    if t == -1:
        return v + 'ed'
    if t == 0:
        if pl:
            return v
        else:
            return v + 's'
    if t == 1:
        return 'will' + ' ' + v


n_list = ('cat', 'dog', 'python', 'toad')
det_list = ('a', 'the', 'my', 'your', 'their')
v_list = (('walk', 1), ('sleep', 1), ('bark', 1), ('meow', 1), ('chill', 1), ('hug', 2), ('help', 2), ('love', 2), ('present', 3), ('show', 3))

t = randint(-1, 1)
v_ = choice(v_list)
args = [(choice(det_list), choice(n_list), randint(0, 1)) for i in range(v_[1])]
sentence = get_np(*args[0]) + ' ' + get_vp(v_[0], t, args[0][2]) + ' ' + ' '.join([get_np(*arg) for arg in args[1:]])
print(sentence)
