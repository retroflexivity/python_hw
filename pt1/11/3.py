def twodigit(num):
    if len(str(num)) == 1:
        return '0' + num
    else:
        return num


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

txt = input('Введите дату. Можно указывать с нулями и без нулей в начале,\
            с месяцем цифрами или буквами и годом с сотнями и без.\n')

date = txt.split('-')
date[0] = twodigit(date[0])
if date[1].isnumeric():
    date[1] = twodigit(date[1])
else:
    date[1] = twodigit(str(months.index(date[1]) + 1))
date[2] = date[2][-2:]

print(date[0] + '-' + date[1] + '-' + date[2])
