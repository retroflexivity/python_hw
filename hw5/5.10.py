import re
bookname = 'pg66655.txt'
started = words = pars = 0

with open(bookname) as book:
    for line in book:
        if re.findall(' *A STORY ABOUT MYSELF *', line):
            started = True
        if started:
            if line == '\n':
                pars += 1
            else:
                words += line[:-1].count(' ') + 1

print(words / pars)
