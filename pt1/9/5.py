from json import loads


def getvalue(tup):
    return tup[1]


with open('laureate.json', encoding='utf-8') as f:
    laureates = loads(f.read())['laureates']

countries = {}
for pers in laureates:
    if (cn := pers.get('bornCountry')) is not None:
        if cn in countries.keys():
            countries[cn] += 1
        else:
            countries[cn] = 1

for tup in sorted(countries.items(), reverse=True, key=getvalue)[:10]:
    print(tup[0])
