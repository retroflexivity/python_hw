rownum = int(input())
with open('borodino.txt', encoding='utf-8') as verse:
    with open('borodinolines.txt', 'w', encoding='utf-8') as output:
        lines = verse.readlines()

        if rownum >= len(lines):
            print('Too much')
        else:
            for i in range(1, rownum + 1): #первая строка — "БОРОДИНО"
                print(lines[i], end = '')
