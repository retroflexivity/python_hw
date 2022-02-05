from csv import DictReader

i = 0
with open('lemur_data.csv', 'r', encoding='unicode_escape') as csv:  # там какая-то ошибка с декодингом
    reader = DictReader(csv)
    for line in reader:
        if line['dam_name'] != 'WHITE-TAIL':
            print(line['name'])
