import string

from .search_utils import load_movies, DEFAULT_SEARCH_LIMIT


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    result = []
    for movie in movies:
        title_tokens = tokenize_text(movie["title"])
        query_tokens = tokenize_text(query)
        if has_matching_token(query_tokens, title_tokens):
            result.append(movie)
            if len(result) >= limit:
                break
    return result

def has_matching_token(query_tokens:list[str], title_tokens:list[str]) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False


def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    text = text.translate(text.maketrans("", "", string.punctuation))
    return text


def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split(" ")
    valid_tokens = []
    for token in tokens:
        if token:
            valid_tokens.append(token)
    return valid_tokens
