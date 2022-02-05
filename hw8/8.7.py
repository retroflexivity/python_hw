gradelist = {}

with open('exam_1.txt', encoding='utf-8') as f:
    for line in f:
        gradelist.update({line.split()[0]: int(line.split()[1])})

with open('exam_2.txt', encoding='utf-8') as f:
    for line in f:
        if (st := line.split()[0]) in gradelist:
            if (mk := int(line.split()[1])) > gradelist[st]:
                gradelist[st] = mk
        else:
            gradelist.update({line.split()[0]: int(line.split()[1])})

for i in sorted(gradelist.items()):
    print(i[0] + ':', i[1])
