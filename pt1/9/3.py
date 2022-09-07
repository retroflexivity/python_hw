def divtest(nums, divisor):
    found = False
    multiples = set()
    for i in nums:
        if i % divisor == 0:
            multiples.add(i)
            found = True
    return multiples


print(divtest([1, 2, 3, 4], 5))
