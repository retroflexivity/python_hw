with open('frankenstein.txt', encoding='utf-8') as file:
    words = file.read().lower().split()
    neigh = {}
    for i, word in enumerate(words):
        if word not in neigh.keys():
            neigh[word] = []
        if i - 1 > 0:
            neigh[word].append(words[i - 1])
        if i + 1 < len(words):
            neigh[word].append(words[i + 1])

for key in neigh:
    neigh[key] = sorted(neigh[key])[:5]

neigh
