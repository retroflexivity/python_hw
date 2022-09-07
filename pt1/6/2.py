with open('ls.txt', encoding='utf-8') as ls:
    for filename in ls:
        if filename != '6.2.py\n' and filename != 'ls.txt\n':

            with open(filename[:-1], encoding='utf-8') as code:
                lines = code.readlines()
                print(filename)

            with open(filename[:-1], 'w', encoding='utf-8') as code:
                for line in lines:
                    code.write(line.replace('	', '    '))
