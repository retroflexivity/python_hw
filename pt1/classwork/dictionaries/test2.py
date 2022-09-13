from csv import DictReader

olympics = DictReader(open('olympics.csv'))
for country in olympics:
    if int(country[' Winter - Total']) > int(country['Summer - Total']):
        print(country['Country'])
