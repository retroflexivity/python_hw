from sklearn.feature_extraction.text import TfidfVectorizer
import logging

logger = logging.getLogger(__file__)

def get_matrix(texts: list[str]) -> None:
    tfidf = TfidfVectorizer(stop_words="english")
    logger.info("TF-IDF matrix...")
    matrix = tfidf.fit_transform(texts)
    logger.info(f"Матрица на {matrix.shape[0]} документов и {matrix.shape[1]} термов")
    return tfidf, matrix
