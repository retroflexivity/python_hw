# мне жаль, что я не должен прикрепить сюда несколько творений по гироскопии и эстетике

words = 0

for i in ('1', '2', '3', '4', '5'):
    with open(i + '.txt', encoding='utf-8') as file:
        for line in file.readlines()[2:]:
            words += line[:-1].count(' ') + 1
print(words / 5)
