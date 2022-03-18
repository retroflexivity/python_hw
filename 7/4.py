def translit(cyrillic):
    table = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
             'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
             'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
             'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
             'ы': 'i', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    latin = ''
    for ch in cyrillic:
        if ch.lower() in table:
            if ch.isupper():
                latin += table[ch.lower()].capitalize()
            else:
                latin += table[ch]

        else:
            latin += ch
    return latin


translit('Жизнь')
