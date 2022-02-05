from string import punctuation


freqlist = {}
for ch in punctuation:
    freqlist.update({ch: 0})


while True:
    text = input('Введите текст\n')
    if text == 'отстань':
        break
    else:
        for ch in text:
            if ch in freqlist:
                freqlist[ch] += 1

print(freqlist)
