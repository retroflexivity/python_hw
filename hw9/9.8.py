from json import loads

with open('laureate.json', encoding='utf-8') as f:
    laureates = loads(f.read())['laureates']

for pers in laureates:
    if (pers.get('bornCountry') != 'Germany'):
        found = False
        for prize in pers['prizes']:
            for aff in prize['affiliations']:
                if isinstance(aff, dict) and aff.get('country') == 'Germany':
                    print(pers['firstname'], pers['surname'])
                    found = True
                    break
            if found:
                break
