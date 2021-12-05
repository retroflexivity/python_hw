def max4n8 (a, b, c, d):
    max = a
    for i in (b, c, d, 8):
        if i > max:
            max = i
    return(max)

print(max4n8(2, 3, 9, 5))
