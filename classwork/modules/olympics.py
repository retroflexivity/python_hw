from csv import DictReader

max = 0
olympics = DictReader(open('olympics.csv'))
for country in olympics:
    if int(country['# Winter']) > max:
        max = int(country['# Winter'])
print(max)

max = ['', 0]
olympics = DictReader(open('olympics.csv'))
for country in olympics:
    if int(country['# Winter']) > max[1]:
        max = [country['Country'], int(country['# Winter'])]
print(max[0])

olympics = DictReader(open('olympics.csv'))
for country in olympics:
    if country['# Summer'] != '0' and country['# Winter'] == '0':
        print(country['Country'])
