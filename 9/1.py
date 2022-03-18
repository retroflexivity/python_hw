def setmath(a, b, isUnion=True):
    if isUnion:
        return(a.union(b))
    else:
        return(a.intersection(b))


setmath({1, 2, 3}, {2, 3, 4}, False)
