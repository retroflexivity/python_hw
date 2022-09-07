#мне сказали, если писать, что вводить, ассистентам приятнее проверять)

fst = [int(n) for n in input('Введите оценки первого студента в строку').split()]
fstAvg = sum(fst)/len(fst)

snd = [int(n) for n in input('Введите оценки второго студента в строку').split()]
sndAvg = sum(snd)/len(snd)

if fstAvg == sndAvg:
    print('Оценки студентов равны')
else:
    print('Студент', int(sndAvg > fstAvg) + 1)
