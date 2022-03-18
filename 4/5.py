one = input()
two = input()
i = j = correct = skipi = skipj = 0

while i < len(one) and j < len(two):

    if skipi or skipj:
        if skipi:
            if one[i] == ' ':
                skipi = 0
            i += 1
        if skipj:
            if two[j] == ' ':
                skipj = 0
            j += 1

    else:
        if one[i] != two[j]:
            skipi = skipj = 1
        elif one[i] == ' ':
            correct += 1
        i += 1
        j += 1

if not (skipi or skipj):
    correct += 1

print(correct)
#а что, можно было сплит использовать?
