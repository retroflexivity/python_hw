from json import loads

with open('laureate.json', encoding='utf-8') as f:
    laureates = loads(f.read())['laureates']

for pers in laureates:
    nomyear = max([int(prize['year']) for prize in pers['prizes']])
    deathyear = int(pers['died'].split('-')[0])
    if (deathyear != 0) and (deathyear - nomyear <= 1):
        print(pers['firstname'], pers['surname'])
