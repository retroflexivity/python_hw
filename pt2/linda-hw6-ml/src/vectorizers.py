import numpy as np

def get_tfidf_vector(tokens: list[str], text_id: int, matrix, tfidf) -> np.ndarray:
    tfidf_vector = np.ndarray(len(tokens))
    # a vector with all the terms
    text_raw_vector = matrix[text_id, :]
    # leaving only terms that are present in the text
    for i in range(len(tokens)):
        idx = tfidf.vocabulary_.get(tokens[i])
        val = matrix[text_id, idx] if idx else 0
        tfidf_vector[i] = val
    # vector with tfidf values of each word in the text
    return tfidf_vector