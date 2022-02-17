from csv import DictReader

lines = DictReader(open('gore_out_uma_by_line.csv', encoding='utf-8'))
correctlines = []
for line in lines:
    ratings = {}
    for rating in [line[src] for src in ['RuSentiLex', 'EmoLex', 'LinisCrowd', 'ChenSkiena', 'ProductSentiRus', 'SentiRusColl', 'Eduard']]:
        if rating not in ratings.keys():
            ratings[rating] = 1
        else:
            ratings[rating] += 1

    if max(ratings.values()) >= 4:
        correctlines.append(line['line lemmas'])

freqlist = {}
for line in correctlines:
    for word in line.split():
        if word not in freqlist:
            freqlist[word] = 1
        else:
            freqlist[word] += 1

freqlist
