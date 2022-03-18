def func(start, end, iseven=False):
    sum = 0
    for i in range(start + ((start % 2) == iseven), end + ((end % 2) != iseven), 2):
        sum += i
    return sum


func(1, func(1, func(1, func(1, func(1, func(1, 10))))))
