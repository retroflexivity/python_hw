n = int(input())
fobr = ""

if not(n % 3):
    fobr += "foo"
if not(n % 5):
    fobr += "bar"

print(fobr)
