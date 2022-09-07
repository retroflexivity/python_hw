def symdif(a, b):
    a = set(a)
    b = set(b)
    return a.union(b) - a.intersection(b)


symdif([1, 2, 3, 3], [2, 4])
