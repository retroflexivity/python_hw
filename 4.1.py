num = input()
odd = even = 0

for i in num:
    if i != '0':
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1

print('Чётных цифр:', even, 'нечётных цифр:', odd)
