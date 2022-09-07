bookname = '4300-0.txt'
words = 0

with open(bookname, encoding='utf-8') as book:
    for line in book:
        words += (wordsinline := line[:-1].count(' ') + 1)
        print(wordsinline)

print('Всего:', words)
