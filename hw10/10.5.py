matrix = {}

while True:
    inp = input()
    if not inp:
        break

    a, b = [int(i) for i in inp.split()]
    if matrix.get(a):
        matrix[a].add(b)
    else:
        matrix[a] = {b}
    if matrix.get(b):
        matrix[b].add(a)
    else:
        matrix[b] = {a}


for i in range(acount := max(matrix) + 1):
    if matrix.get(i):
        for j in range(acount):
            if j in matrix[i]:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()
    else:
        print('0 ' * acount)
