def palindrome(word):
    vowels = 'aeiouаеёиоуыэюя'
    word = word.replace('ь', '').replace('ъ', '')
    if len(word) <= 1:
        return True
    else:
        if (word[0] in vowels) == (word[-1] in vowels):
            return palindrome(word[1:-1])
        else:
            return False


palindrome('палиндромом')
