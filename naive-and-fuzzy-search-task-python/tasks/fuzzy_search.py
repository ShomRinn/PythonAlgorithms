"""Templates for programming assignments: fuzzy search."""
from typing import List


def find_levenshtein_distance(string_a: str, string_b: str) -> int:
    """Returns the Levenshtein distance between two strings.

    Args:
        string_a: str, the first string.
        string_b: str, the second string.
    
    Returns:
        int, the Levenshtein distance between the given strings.
    """
    if len(string_a) < len(string_b):
        return find_levenshtein_distance(string_b, string_a)

    if len(string_b) == 0:
        return len(string_a)

    previous_row = range(len(string_b) + 1)
    for i, char_a in enumerate(string_a):
        current_row = [i + 1]
        for j, char_b in enumerate(string_b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (char_a != char_b)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


class FuzzySearchEngine:
    """Provides a basic 'FuzzySearch engine' interface."""
    def __init__(self):
        self.corpus = []

    def load_corpus(self, corpus: List[str]):
        """Loads a given corpus of texts.

        Args:
            corpus: List[str], a set of texts that will be used as a database for the engine.
        """
        self.corpus = corpus
    
    def find_best_matches(self, query_text: str, n_results: int = 1) -> List[str]:
        """Returns the most similar texts from the corpus based on a query text.

        NOTE: Please use the Levenshtein distance to measure the similarity between strings.
        NOTE: If there are multiple texts with the same Levenshtein distance for the query text 
        within the corpus, order the results lexicographically.
        NOTE: If the corpus contains less than 'n_results' texts, please return all the available ones.

        Args:
            query_text: str, a query text that should be used to retrieve texts from the corpus.
            n_results: int, the number of texts that should be returned (the most similar ones).
        Returns:
            List[str], the best matches from the corpus.
        """
        if not self.corpus:
            return []

        distances = [(text, find_levenshtein_distance(query_text, text)) for text in self.corpus]
        distances.sort(key=lambda x: (x[1], x[0]))  # Sort by distance and then lexicographically

        return [text for text, _ in distances[:n_results]]
