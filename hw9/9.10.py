from csv import DictReader
from json import dumps

dict = list(DictReader(open('csv.csv', encoding='utf-8')))
with open('json.json', 'w', encoding='utf-8') as jfile:
    jfile.write(dumps(dict, ensure_ascii=False, indent=4))
