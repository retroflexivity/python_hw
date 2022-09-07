mpn = []

print('Вводите грузинские слова в столбик. В конце нажмите "ввод"')
while True:
    word = input()
    if word == "":
        break

    if word[-3:-1] == 'eb':
        mpn.append(word)

for i in sorted(mpn):
    print(i)
