from string import punctuation
from re import match
punctuation += '«»”'

with open('povest_cleansed.txt', encoding='utf-8') as f:
    text = f.read()

words = set()
for word in [word.strip(punctuation) for word in text.split()]:
    if match('[А-ЯѢ]', word):
        words.add(word)

print(words)

вавилон
