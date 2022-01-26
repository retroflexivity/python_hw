import json
with open('countries.json', 'r', encoding='utf-8') as file:
    list = json.load(file)

regions = {}
list = list[1]
for i in list:
    if i['region']['value'] in regions:
        regions[i['region']['value']] += 1
    else:
        regions[i['region']['value']] = 1

print(regions)
