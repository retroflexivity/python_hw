from csv import DictReader

olympics = DictReader(open('olympics.csv'))
for country in olympics:
    if country['Country'] != 'Totals' and int(country['Combined total']) > 50:
        print(country['Country'])
