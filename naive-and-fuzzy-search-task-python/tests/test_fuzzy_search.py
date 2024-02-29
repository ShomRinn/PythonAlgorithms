"""Sample tests for 'tasks.fuzzy_search' module."""
from tasks.fuzzy_search import find_levenshtein_distance, FuzzySearchEngine


def test_find_levenshtein_distance_sample():
    """Tests for find_levenshtein_distance function."""
    assert find_levenshtein_distance("property", "attribute") == 8
    assert find_levenshtein_distance("maximization", "minimization") == 2
    assert find_levenshtein_distance("confusion", "induction") == 5


def test_fuzzy_search_engine_sample():
    """Tests for FuzzySearchEngine class."""
    fse = FuzzySearchEngine()
    fse.load_corpus([
        "refund",
        "spy",
        "retailer",
        "concede",
        "dozen",
    ])

    assert fse.find_best_matches("recruit", n_results=3) == [
        "refund", "retailer", "concede",
    ]
    assert fse.find_best_matches("button", n_results=3) == [
        "dozen", "refund", "spy",
    ]
