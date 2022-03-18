def conv (name):
    return {
        "rock": 0,
        "paper": 1,
        "scisors": 2,
    }[name]

pl1 = input()
pl2 = input()

pl1 = conv(pl1)
pl2 = conv(pl2)

print ({
    0: "draw",
    1: "pl1",
    -2: "pl1",
    -1: "pl2",
    2: "pl2",
}[pl1 - pl2])
