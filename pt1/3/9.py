import math
sides = [0, 0, 0]

sides[0] = float(input())
sides[1] = float(input())
sides[2] = float(input())

for i in range(2):
    if sides[i] > sides[2]:
        tmp = sides[i]
        sides[i] = sides[2]
        sides[2] = tmp

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print(sides[0]*sides[1]/2)
else:
    print("Вы огорчили Евклида")
