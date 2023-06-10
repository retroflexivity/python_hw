from re import sub
def clean_tokenize(text: str) -> list[str]:
    return sub(f'\s+', ' ', sub(r'(<[^>]*>)|[^\w\s]', '', text.lower())).split()

def count_token_freq(tokens: list[str], freq_dict: dict[str, int], token_amount_counter: list[int]) -> None:
    """
    `token_amount_counter` is a 'pointer parody'. Idk how to pass a counter into a function.
    think of it as of an int value that is passed by reference
    """
    for t in tokens:
        token_amount_counter[0] += 1
        if t in freq_dict: freq_dict[t] += 1
        else: freq_dict[t] = 1

from nltk.corpus import stopwords as StopWords
stop_words = set(StopWords.words('english'))

def stopword_filtering(tokens: list[str]) -> list[str]:
    return [tkn for tkn in tokens if not tkn in stop_words]

from nltk.corpus import wordnet as wn

def do_stemming(tokens: list[str]) -> None:
    """In place"""
    for i in range(len(tokens)):
        result = wn.morphy(tokens[i])
        if result:
            tokens[i] = result

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def do_lemmatizing(tokens: list[str]) -> None:
    """In place"""
    for i in range(len(tokens)):
        tokens[i] = lemmatizer.lemmatize(tokens[i])

def remove_lowfreq(text: str, forms_to_remove: set[str], new_token_amount_counter: list[int]) -> str:
    """
    `new_token_amount_counter` is a 'pointer parody'. Idk how to pass a counter into a function.
    think of it as of an int value that is passed by reference
    """
    new_tokens = [tkn for tkn in text.split() if not tkn in forms_to_remove]
    new_token_amount_counter[0] += len(new_tokens)
    return ' '.join(new_tokens)

def preprocess(text: str, config: dict, freq_dict: dict[str], token_counter: list[int]) -> str:
    tokens = clean_tokenize(text)
    if config['DO_STEMMING']: do_stemming(tokens)
    if config['LEMMATIZE']: do_lemmatizing(tokens)
    if config['STOPLIST']: tokens = stopword_filtering(tokens)
    if config['LOWFREQ_FILTER']: count_token_freq(tokens, freq_dict, token_counter)
    return ' '.join(tokens)