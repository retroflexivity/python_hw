import re

dict = {}
with open('1.txt', encoding='utf-8') as f:
    for line in f:
        name = re.search(r'[а-яА-ЯёЁ]*', line).group(0)
        number = int(re.search(r'\d+', line).group(0))
        if name in dict:
            dict[name] += number
        else:
            dict[name] = number

print(dict)
