from csv import DictReader


def matches(value, rule):
    if value.isnumeric() and not rule.isnumeric():
        value = int(value)
        if rule[-1] == '+':
            if value >= int(rule[:-1]):
                return True
        elif rule[-1] == '-':
            if value <= int(rule[:-1]):
                return True
        elif '-' in rule and rule.replace('-', '').isnumeric():
            if int(rule.split('-')[0]) < value < int(rule.split('-')[1]):
                return True

    elif rule.lower() in value.lower():
        return True

    return False


rules = {}
print('Name, Alignment, Gender, EyeColor, Race, HairColor, Publisher, SkinColor, Height, Weight')
for i in range(3):
    rules.update({input('Введите критерий ' + str(i + 1) + ': '): input('Введите значение: ')})


with open('marvel_characters_info.csv', encoding='utf-8') as f:
    heroes = DictReader(f)

    for hero in heroes:
        ok = True
        for rule in rules.items():
            if not matches(hero[rule[0]], rule[1]):
                ok = False
                break
        if ok:
            print(hero['Name'], [hero[rule[0]] for rule in rules.items()])
