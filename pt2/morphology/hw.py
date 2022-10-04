# %% codecell
from pymystem3 import Mystem
from pymorphy2 import MorphAnalyzer
m = Mystem()
morph = MorphAnalyzer()
with open('book.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# %% codecell
lemmas = m.lemmatize(text)
with open('lemmas.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(lemmas))

# %% codecell
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
tokens = [w.lower() for w in tokens if w.isalpha()]

# %% codecell
from json import dumps
an_list = []
with open('parse.jsonl', 'w', encoding='utf-8') as f:
    for word in tokens:
        ana = morph.parse(word)[0]
        f.write(dumps({'lemma': str(ana.normal_form), 'word': str(ana.word), 'pos': str(ana.tag.POS)}, ensure_ascii=False) + '\n')
        an_list.append((str(ana.normal_form), str(ana.tag.POS)))

# %% codecell
from nltk.corpus import stopwords
sw = stopwords.words('russian')

pos_freq = {}
verbs = {}
adverbs = {}
for word in an_list:
    if word not in sw:
        if word[1] != 'None':
            pos_freq[word[1]] = pos_freq.get(word[1], 0) + 1
        if word[1] in ('VERB', 'INFN', 'PRTF', 'PRTS', 'GRND'):
            verbs[word[0]] = verbs.get(word[0], 0) + 1
        elif word[1] in ('ADVB', 'PRED'):
            adverbs[word[0]] = adverbs.get(word[0], 0) + 1

# %% codecell
for pos in sorted(pos_freq.items(), key=lambda x: x[1], reverse=True):
    print(pos[0], round((pos[1] / len(an_list)), 4))

# %% codecell
print(*sorted(verbs, key=verbs.get, reverse=True)[:20], sep='\n')

# %% codecell
print(*sorted(adverbs, key=adverbs.get, reverse=True)[:20], sep='\n')


# %% codecell
def ngrams(key):
    nglist = {}
    for ng in key((word[0] for word in an_list)):
        nglist[ng] = nglist.get(ng, 0) + 1

    return '\n'.join((' '.join(ng) for ng in sorted(nglist, key=nglist.get, reverse=True)[:25]))


# %% codecell
from nltk import bigrams
print(ngrams(bigrams))

# %% codecell
from nltk import trigrams
print(ngrams(trigrams))

# %% codecell
paragraph = [word for word in word_tokenize(text.split('\n')[156])]


# %% codecell
def flip(word):
    ana = morph.parse(word)[0]

    if ana.tag.POS in ('NOUN', 'ADJF', 'PRTF'):
        if ana.tag.number == 'sing' and 'Sgtm' not in ana.tag:
            return ana.inflect({'plur'}).word
        if ana.tag.number == 'plur' and 'Pltm' not in ana.tag:
            return ana.inflect({'sing'}).word

    if ana.normal_form in ('он', 'она', 'оно'):
        return morph.parse('они')[0].inflect({ana.tag.case}).word

    if ana.normal_form == 'они':
        return morph.parse('оно')[0].inflect({ana.tag.case}).word

    if ana.tag.POS == 'VERB':
        if ana.tag.aspect == 'perf':
            if ana.tag.tense == 'past':
                ana = ana.inflect({'futr', '3per'})
            else:
                ana = ana.inflect({'past'})
        if ana.tag.aspect == 'impf':
            if ana.tag.tense == 'past':
                ana = ana.inflect({'pres', '3per'})
            else:
                ana = ana.inflect({'past'})

        if ana.tag.number == 'sing':
            return ana.inflect({'plur'}).word
        else:
            return ana.inflect({'sing'}).word

    return word


# %% codecell
flipped = ''
for word in paragraph:
    if word[0].isalpha() or word == '-':
        flipped += ' '
    flipped += flip(word)

flipped[1:]
