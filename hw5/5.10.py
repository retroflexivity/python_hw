bookname = '4300-0.txt'
book = open(bookname)
words = pars = 0

for line in book:
    # print(line)
    if line == '\n':
        pars += 1
    else:
        words += line[:-1].count(' ') + 1

print(pars, words, words / pars)
