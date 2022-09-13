from json import loads
from re import split, search


def splitentry(word, entry):
    list = []
    synonym = search(', [А-ЯЁӇ]{2,999}', entry)
    if synonym:
        list.append((word, split(r'(?<=\. )[IV]+ ?', entry.replace(synonym.group(), ''))))
        list.append((synonym.group()[2:], split(r'(?<=\. )[IV]+ ?', entry[synonym.span()[1]:].replace(synonym.group(), ''))))
    else:
        list.append((word, split(r'(?<=\. )[IV]+ ?', entry)))
    return list


with open('Even.json', encoding='utf-8') as f:
    json = loads(f.read())

dsl = []
for word in json:
    for e in splitentry(word, json[word]):
        for g in e[1]:
            dsl.append((e[0], g))

with open('Even.dsl', 'w', encoding='utf-8') as f:
    for entry in dsl:
        f.write(entry[0] + '\n  ' + '[b]' + entry[0] + '[\\b] ' + entry[1].strip('I') + '\n')
