bookname = '4300-0.txt'
book = open(bookname)
words = 0

for line in book:
    words += (wordsinline := line[:-1].count(' ') + 1)
    print(wordsinline)

print('Всего:', words)
