dict = {}

while True:
    inp = input()
    if not inp:
        break
    school, grade = inp.split()[2:]
    if school in dict:
        dict[school][0] += int(grade)
        dict[school][1] += 1
    else:
        dict[school] = [int(grade), 1]

max = 0
for school in dict:
    if dict[school][0] / dict[school][1] > max:
        maxnum = school
        max = dict[school][0] / dict[school][1]

print('Школа:', maxnum)
print('Средний результат:', max)
