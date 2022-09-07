capvows = 'AEIOU'
bookname = '4300-0.txt'
words = 0

with open(bookname, encoding='utf-8') as book:
    for line in book:
        for word in line.split():
            if word[0] in capvows:
                print(word)
                words += 1

print('Всего', words)
