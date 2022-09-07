def jumble(word):
    from random import sample
    return word[0] + ''.join(sample(word[1:-1], len(word) - 2)) + word[-1]

jumble('ретрофлексивность')
