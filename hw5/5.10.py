bookname = 'pg66655.txt'
book = open(bookname)
words = pars = 0

for line in book:
    if line == '\n':
        pars += 1
    else:
        words += line[:-1].count(' ') + 1

print(words / pars)
