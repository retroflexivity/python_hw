with open('kartowka.txt', 'a', encoding='utf-8') as kartowka:
    pass

with open('kartowka.txt', encoding='utf-8') as kartowka:
    if (len(lines := kartowka.readlines()) > 0) and lines[0] != '':
        print(len(lines))
    else:
        print('Нет такого файла')
