pl1 = input()
pl2 = input()

if pl1 == "камень":
    pl1 = 0
elif pl1 == "бумага":
    pl1 = 1
else:
    pl1 = 2

if pl2 == "камень":
    pl2 = 0
elif pl2 == "бумага":
    pl2 = 1
else:
    pl2 = 2

if (outcome := (pl1 - pl2) % 3) == 0:
    print("ничья")
elif outcome == 1:
    print("победил игрок 1")
else:
    print("победил игрок 2")
