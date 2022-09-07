from csv import DictReader

dict = list(DictReader(open('SuperHeroes.csv', encoding='utf-8'), delimiter=';'))

htlist = []
total = count = 0

for hero in dict:
    if hero.get('Race') == 'Human':
        if hero.get('Height'):
            htlist.append(float(hero['Height']))

htlist.sort()
median = (htlist[int(len(htlist) / 2)] + htlist[round(len(htlist) / 2)]) / 2

for hero in dict:
    if hero.get('Alignment') == 'bad' and hero.get('Race') == 'Human':
        count += 1
        if hero.get('Height'):
            total += float(hero['Height'])
        else:
            total += median

print(total / count)
