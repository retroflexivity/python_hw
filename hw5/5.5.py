puntctlist = '.,?!:;'
words = input('Введите предложение').split()

punct = 0
for word in words:
    for char in word:
        if char in puntctlist:
            punct += 1
            break

print('Всего слов: ' + str(len(words)) + ', со знаками: ' + str(punct) + ', доля: ' + str(round(punct / len(words) * 100, 2)) + '%')
