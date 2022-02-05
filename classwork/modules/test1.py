from csv import DictReader

olympics = DictReader(open('olympics.csv'))
for country in olympics:
    if country['Country'].startswith('Brazil'):
        print(country['Combined total'])
