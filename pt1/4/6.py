#сплит так сплит

nums = input().split()
total = 0
avg = 0.0
sorted = ''
for i in nums:
    avg += int(i)
avg /= len(nums)

for i in range(int(avg) - int(int(avg) + 1 - avg), int(avg+2)): #настроение неимпортовое
    inst = nums.count(str(i))
    for j in range(inst):
        sorted += str(i) + ' '
    total += inst

print(total)
print(sorted)
