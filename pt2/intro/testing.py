size, target = [int(i) for i in input().split()]
matrix = [[int(n) for n in input().split()] for row in range(size)]

res = []
for col in range(size):
    res.append(sorted([row[col] for row in matrix], key=lambda x: (abs(target - x), x)))


print('\n'.join([' '.join([str(row[col]) for row in res]) for col in range(size)]))
