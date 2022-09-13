import re

with open('2.txt', encoding='utf-8') as f:
    text = f.read()
    dict = {re.search(r'[a-z1-9\-.]*@[a-z1-9\-.]*', text).group(0): re.split(', ', re.search(r'(?<=Тел. ).*(?=( ))', text).group(0))}
    print(dict)
