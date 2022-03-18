def letterpase(filename):
    conslist = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    vowlist = 'aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ'
    yerlist = 'ъьЪЬ'
    consonants = vowels = yers = 0

    with open(filename, encoding='utf-8') as file:
        for line in file:
            for ch in line:
                if ch in conslist:
                    consonants += 1
                elif ch in vowlist:
                    vowels += 1
                elif ch in yerlist:
                    yers += 1

    return(consonants, vowels, yers)


letterpase('testfile.txt')
