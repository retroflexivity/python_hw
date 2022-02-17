from csv import DictReader


def matches(value, rule):
    return True


rules = {}
print('Name, Alignment, Gender, EyeColor, Race, HairColor, Publisher, SkinColor, Height, Weight')
# for i in range(3):
#     rules.update({input('Введите критерий ' + str(i + 1) + ': '): input('Введите значение: ')})

rules = {'Height': '190+', 'Alignment': 'good', 'Publisher': 'Marvel Comics'}

with open('marvel_characters_info.csv', encoding='utf-8') as f:
    heroes = DictReader(f)

    for hero in heroes:
        ok = True
        for rule in rules.items():
            if not matches(hero[rule[0]], rule[1]):
                ok = False
                break
        if ok:
            print(hero['Name'])
