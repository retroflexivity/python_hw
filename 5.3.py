arr = []
sum = 0

while (inp := input('Вводите цену и количество в столбик. В конце нажмите "ввод"')) != "":
    # inp = input()
    # if inp == "":
    #     break
    arr.append([int(n) for n in inp.split()])

for i in arr:
    value = i[0] * i[1]
    print(value)
    sum += value

print('Сумма:', sum)
