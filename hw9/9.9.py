from json import dumps
from string import punctuation
punctuation += '—«»'


def getvalue(tup):
    return tup[1]


with open('lyrics.txt', encoding='utf-8') as f:
    lyrics = f.read()

freqlist = {}
for word in lyrics.split():
    word = word.lower().strip(punctuation)
    if word:
        if word in freqlist:
            freqlist[word] += 1
        else:
            freqlist[word] = 1

count = 0
with open('song_dict.json', 'w', encoding='utf-8') as f:
    f.write(dumps(freqlist, ensure_ascii=False, indent=4, sort_keys=True))

for tup in sorted(freqlist.items(), reverse=True, key=getvalue):
    if count < 10:
        print(tup[0])
        count += 1
