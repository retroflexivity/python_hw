nums = sorted([int(n) for n in input('Введите целые числа в строку').split()])

print((nums[int((len(nums) - 1) / 2)] + nums[int(len(nums) / 2)]) / 2) #зачем я это сделал
