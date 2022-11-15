# %% codecell
from pymystem3 import Mystem
from os import listdir
from nltk import sent_tokenize
from nltk.corpus import stopwords
from re import finditer
m = Mystem()
sw = stopwords.words('russian')

# %% codecell
def ltz(text):
    return ' '.join((word for word in m.lemmatize(text) if any(letter.isalnum() for letter in word) and word not in sw)) + '\n'

# %% codecell
def crop_heading(text):
    fi = finditer('', text)
    next(fi)
    return text[next(fi).start():]

# %% codecell
with open('lemmatized.txt', 'w', encoding='utf-8') as lemmatized:
    for filename in listdir('books'):
        with open('books/' + filename, encoding='koi8-r') as book:
            text = crop_heading(book.read())
            for row in [sent_tokenize(row) for row in text.split('\n')]:
                for sent in row:
                    lemmatized.write(ltz(sent))
                    # print(sent)

# %% codecell
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
from logging import basicConfig, INFO

# %% codecell
basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=INFO)

# %% codecell
data = LineSentence('lemmatized.txt')

# %% codecell
model_fdn = Word2Vec(data, vector_size=300, window=5, min_count=5, epochs=50)

# %% codecell
# model_fdn.init_sims(replace=True)
model_path = "fdn.bin"
model_fdn.wv.save_word2vec_format(model_path, binary=True)

# %% codecell
len(model_fdn.wv)

# %% codecell
model_fdn.wv.most_similar('фандорин')

# %% codecell
model_fdn.wv.most_similar('смерть')

# %% codecell
model_fdn.wv.most_similar(['быстро', 'медленно'])

# %% codecell
model_fdn.wv.doesnt_match(['идти', 'ехать', 'двигаться', 'везти'])

# %% codecell
from gensim.models import KeyedVectors
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
%matplotlib inline
pca = PCA(n_components=2)

# %% codecell
from urllib.request import urlretrieve
url = "http://vectors.nlpl.eu/repository/20/220.zip"
urlretrieve(url, "pre_model.zip")

# %% codecell
import zipfile
with zipfile.ZipFile('pre_model.zip', 'r') as zip_ref:
    zip_ref.extractall('pre_model')

# %% codecell
pre_model = KeyedVectors.load_word2vec_format('pre_model/model.bin', binary=True)

# %% codecell
pre_model.most_similar(positive=['большой_ADJ', 'маленький_ADJ'], negative=['тяжелый_ADJ'], topn=1)[0][0]

# %% codecell
words = ('украина_PROPN', 'япония_PROPN', 'россия_PROPN', 'израиль_PROPN', 'белоруссия_PROPN', 'китай_PROPN', 'германия_PROPN', 'франция_PROPN', 'корея_PROPN', 'вьетнам_PROPN')
coords = pca.fit_transform(pre_model[words])

# %% codecell
[len(pre_model[words][i]) for i in range(len(words))]

# %% codecell
plt.scatter(coords[:, 0], coords[:, 1])
plt.title('countries')

for i, word in enumerate(words):
    plt.annotate(word, xy=(coords[i, 0], coords[i, 1]))
plt.show()

# %% codecell
def synonym(word):
    for entry in pre_model.key_to_index:
        if entry[:entry.find('_')] == word:
            res = pre_model.most_similar(entry)[0][0]
            return res[:res.find('_')]
    return word

# %% codecell
sent = 'Руками он брался за горячий стакан с крепким чаем и передвигал шахматные фигурки.'
''.join((synonym(word) if not word in sw else word for word in m.lemmatize(sent)))[:-1]

# %% codecell
import wikipediaapi
wp = wikipediaapi.Wikipedia('ru')

# %% codecell
from os import mkdir
mkdir('wp')

# %% codecell
def get_articles(category, name):
    i = 0
    for article in category.categorymembers.values():
        if i == art_num:
            return
        if article.ns != wikipediaapi.Namespace.CATEGORY and article.text:
            with open(f'wp/{name}_{article.title}.txt', 'w', encoding='utf-8') as f:
                f.write(ltz(article.text))
                i += 1

# %% codecell
art_num = 10
cats = (('cars', 'Автомобили', '#c70a0a'),
        ('linguistics', 'Лингвистика', '#20ad03'),
        ('literature', 'Литературоведение', '#a614a6'),
        ('mathematics', 'Математика', '#1e2fc7'),
        ('philosophy', 'Философия', '#0bb8b5'),
        ('sociology', 'Социология', '#f2ea07'))

# %% codecell
for c in cats:
    get_articles(wp.page(f'Category:{c[1]}'), c[0])

# %% codecell

# %% codecell
from os import listdir
articles = [open(f'wp/{f}', encoding='utf-8').read() for f in sorted(listdir('wp'))]

# %% codecell
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(analyzer="word", ngram_range=(1, 3), min_df=3)

# %% codecell
matrix = tfidf.fit_transform(articles)

# %% codecell
len(tfidf.get_feature_names())

# %% codecell
from numpy import array, argsort

# %% codecell
def top_words(vector, feature_names, top_n=5):
    sorted_nzs = argsort(vector.data)[:-(top_n+1):-1]
    return feature_names[vector.indices[sorted_nzs]]

# %% codecell
for i, article in enumerate(articles):
    print(cats[i // art_num][0])
    print(', '.join(top_words(matrix[i, :], array(tfidf.get_feature_names()))))

# %% codecell
art_coords = pca.fit_transform(matrix.toarray())

# %% codecell
def plot_cats(catnums, plot):
    for i, cat in zip(catnums, (cats[num] for num in catnums)):
        plot.scatter(art_coords[10 * i:10 * (i + 1), 0], art_coords[10 * i:10 * (i + 1), 1], color=cat[2])

# %% codecell
fig, axs = plt.subplots(2, 2)
fig.suptitle('articles')

plot_cats(range(6),    axs[0, 0])
plot_cats(range(1, 6), axs[0, 1])
plot_cats(range(2, 6), axs[1, 0])
plot_cats(range(3, 6), axs[1, 1])

plt.figlegend([cat[0] for cat in cats], loc='lower right')
plt.show()

# %% codecell
alpha_tfidf = TfidfVectorizer(analyzer="word", token_pattern=r'\b[a-zA-Zа-яА-ЯёЁ]+\b', ngram_range=(1, 3), min_df=3)
alpha_matrix = alpha_tfidf.fit_transform(articles)

# %% codecell
len(alpha_tfidf.get_feature_names())

# %% codecell
from sklearn.metrics.pairwise import cosine_similarity
cos_sim = cosine_similarity(alpha_matrix)
cos_sim.shape

# %% codecell
def cos_most_similar(num):
    return [articles[i] for i in cos_sim[num].argsort()[-2:-5:-1]]

# %% codecell
cos_most_similar(1)

# %% codecell
cos_most_similar(37)

# %% codecell
from seaborn import clustermap
cm = clustermap(cos_sim, col_cluster=False)
