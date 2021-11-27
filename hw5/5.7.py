bookname = '4300-0.txt'
book = open(bookname)
words = 0

for line in book:
        wordsinline = line[:-1].count(' ') + 1
        words += wordsinline
        print(wordsinline)

print(words)
