from

random import choice
hashes = {}
for i in range(10):
    hashes[i] = i ^ 2
hashes

grades = {}
for sn in ['Студент1', 'Студент2', 'Студент3']:
    grades[sn] = choice(list(range(1, 11)))
grades
