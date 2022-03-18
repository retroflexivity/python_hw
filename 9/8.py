from json import loads

with open('laureate.json', encoding='utf-8') as f:
    laureates = loads(f.read())['laureates']

for pers in laureates:
    if (pers.get('bornCountry') != 'Germany'):
        phys = de = False
        for prize in pers['prizes']:
            if prize['category'] == 'physics':
                phys = True
            for aff in prize['affiliations']:
                if isinstance(aff, dict) and aff.get('country') == 'Germany':
                    de = True
        if de and phys:
            print(pers['firstname'], pers['surname'])
