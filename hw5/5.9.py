puntctlist = ['.', '?', '!', '...', '!!', '!!!', '??', '???', '!?', '?!']
import re
bookname = '4300-0.txt'
book = open(bookname)
sents = 0

for line in book:
    for word in line.split(): #так U.S. хотя бы не два предложения, а одно
        for punct in puntctlist:
            if re.search('[^.?!][' + punct + ']', word):
                sents += 1
                break

print(sents)
