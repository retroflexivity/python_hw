capvows = 'AEIOU'
bookname = '4300-0.txt'
book = open(bookname)

for line in book:
    for word in line.split():
        if word[0] in capvows:
            print(word)

print('Всего', words)
