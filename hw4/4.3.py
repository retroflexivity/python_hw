sent = input()
skip = 0
print(sent[0], end = '')

for i in sent[1:]:
    if i.isupper():
        print('NAME', end = '')
        skip = 1
    if not(i.isalpha()):
        skip = 0
    if not skip:
        print(i, end = '')
print()
