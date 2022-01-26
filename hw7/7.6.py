from string import punctuation

text = "the cat is hidden in the hat"


def tokenize(string):
    for punct_c in punctuation:
        string = string.replace(punct_c, ' ')  # реплейс использовался на неправильной переменной
    string_tokens = string.split()
    return string_tokens


string = "the cat sat on the mat"
print(tokenize(string))
