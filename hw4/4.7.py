even = 0
while True:
    num = input()
    if num == "":
        break
    if int(num) % 2 == 0:
        even += 1
if even:
    print(even)
else:
    print('-1')
