from re import split
from string import punctuation


def wordsbysentence(filename):
    stlist = []
    with open(filename, encoding='utf-8') as f:
        sentences = split('\\u002e|\\u0021|\\u003f', f.read())
        for sentence in sentences:
            stwords = set()
            for word in sentence.split():
                word = word.strip(punctuation)
                if word != '':
                    stwords.add(word)
            stlist.append(stwords)
    return stlist


print(wordsbysentence('pg66655.txt'))
