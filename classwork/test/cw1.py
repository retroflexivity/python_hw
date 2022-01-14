cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
str = input('Введите текст для проверки\n')

for ch in str:
    if ch.isalpha():
        if ch.lower() in cyrillic:
            print('Буква', ch, 'родная кириллическая')
        else:
            print('Буква', ch, 'иностранный агент!!!!!!!!!')
