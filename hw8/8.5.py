def getvalue(tup):
    return tup[1]


freqlist = {}

while True:
    text = input('Введите текст\n')
    if text == 'отстань':
        break
    else:
        for ch in text:
            if ch in freqlist:
                freqlist[ch] += 1
            else:
                freqlist.update({ch: 1})

print(sorted(freqlist.items(), reverse=True, key=getvalue))
