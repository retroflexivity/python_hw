bookname = '4300-0.txt'
book = open(bookname)
words = 0

for line in book:
        words += wordsinline := line.count(' ')
        print(wordsinline)

print(words)
