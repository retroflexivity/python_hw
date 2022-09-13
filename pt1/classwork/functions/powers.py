def foo(*args):
    out = []
    for num in args:
        out.append(num ** (num % 2 + 2))
    return(out)

print(foo(1, 2, 3, 4))
