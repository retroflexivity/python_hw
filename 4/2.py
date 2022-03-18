num = int(input())
prim = 1

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i)
        prim = 0

if prim:
    print('-1')
