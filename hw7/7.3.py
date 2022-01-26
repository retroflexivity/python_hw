def romandecoder(roman):
    digits = 'ivxlcdm'
    arabic = buffer = 0
    for ch in roman.lower():
        if ch not in digits:
            return 'Не число.'
        else:
            value = (10 ** (digits.index(ch) // 2)) * (5 ** (digits.index(ch) % 2))
            if value <= buffer:
                arabic += buffer
            else:
                arabic -= buffer
            buffer = value
    return arabic + buffer


romandecoder('mcmxvii')
