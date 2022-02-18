def addheight(member):
    dict[member][0] += 1
    for child in dict[member][1:]:
        addheight(child)


dict = {}

for i in range(int(input()) - 1):
    child, parent = input().split()

    if not dict.get(parent):
        dict[parent] = [0]
    dict[parent].append(child)

    if not dict.get(child):
        dict[child] = [dict[parent][0] + 1]
    else:
        addheight(child)

print('\n')
for member in sorted(dict):
    print(member, dict[member][0])
