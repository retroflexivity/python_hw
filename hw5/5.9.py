import re
puntctlist = ['.', '?', '!', '...', '!!', '!!!', '??', '???', '!?', '?!']
bookname = '4300-0.txt'
sents = 0

with open(bookname, encoding='utf-8') as book:
    for line in book:
        for word in line.split():  # так U.S. хотя бы не два предложения, а одно
            for punct in puntctlist:
                if re.search('[^.?!][' + punct + ']', word):
                    sents += 1
                    break

print(sents)
