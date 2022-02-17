from json import dumps, loads
from string import punctuation
punctuation += '—«»'


def getvalue(tup):
    return tup[1]


freqlist = {}
with open('lermontov-maskarad_spoken-text-by-character.json', encoding='utf-8') as f:
    chars = loads(f.read())

for char in chars:
    if char['gender'] == 'FEMALE':
        for line in char['text']:
            for word in line.split():
                word = word.lower().strip(punctuation)
                if word:
                    if word in freqlist:
                        freqlist[word] += 1
                    else:
                        freqlist[word] = 1

with open('lermontov_freqdict.json', 'w', encoding='utf-8') as f:
    f.write('{\n')
    for word in sorted(freqlist.items(), reverse=True, key=getvalue):
        f.write('\t"' + str(word[0]) + '": ' + str(word[1]) + ',\n')  # как это делать нормально
    f.write('}')
