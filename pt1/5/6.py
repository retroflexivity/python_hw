bookname = '4300-0.txt'
booklines = (file := open(bookname, encoding="utf-8")).readlines()
file.close()

print('# https://gutenberg.org/files/4300/4300-0.txt')
print(bookname)
# так, что ли? странное задание
print(len(booklines))
