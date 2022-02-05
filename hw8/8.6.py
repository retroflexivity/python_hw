import matplotlib.pyplot as plt


def getvalue(tup):
    return tup[1]


freqlist = {}

filename = input('Введите полное имя файла\n')
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        for ch in line:
            ch = "'" + ch + "'"
            if ch != '\n':
                if ch in freqlist:
                    freqlist[ch] += 1
                else:
                    freqlist.update({ch: 1})


flsorted = sorted(freqlist.items())
keys = [i[0] for i in flsorted]
values = [i[1] for i in flsorted]

fig, ax = plt.subplots()
ax.bar(keys, values)
fig.set_figwidth(30)
fig.set_figheight(10)
plt.savefig('freqlist.png', dpi=300, bbox_inches='tight')
