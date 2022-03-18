from re import findall

countries = {
             7: 'России',
             73: 'России',
             74: 'России',
             76: 'Казахстана',
             77: 'Казахстана',
             78: 'России или Казахстана',
             79: 'России',
             992: 'Таджикистана',
             993: 'Туркмении',
             994: 'Азербайджана',
             995: 'Грузии',
             996: 'Киргизии',
             997: 'Казахстана',
             998: 'Узбекистана',
            }

error = 'Телефон введен неверно'

num = input('Введите номер телефона.\n')
if num[0] == '8':
    num = '+7' + num[1:]
elif num[:2] == '00':
    num = '+' + num[2:]

if num[:2] != '+7' and num[:2] != '+9':
    print(error)
else:
    num = ''.join(findall(r'\d', num))
    if len(num) < 11 or len(num) > 13:
        print(error)
    ccode = num[:-10]
    rcode = num[-10:-7]
    mainpart = num[-7:]

    if not countries.get(int(ccode)):
        print(error)
    else:
        print(
              'Телефон +' + ccode + '(' + rcode + ')'
              + mainpart[:3] + '-' + mainpart[3:5] + '-' + mainpart[5:]
              + ' из ' + countries[int(ccode)]
             )
