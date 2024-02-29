"""Sample tests for "tasks.prefix_tree" module."""
from tasks.prefix_tree import PrefixTree, PrefixTreeAugmented, get_number_of_matches


def test_prefix_tree_sample():
    """Tests for PrefixTree class."""
    pt = PrefixTree()
    pt.insert("aba")
    pt.insert("aba")
    pt.insert("abab")
    pt.insert("caba")

    assert not pt.search("a")
    assert not pt.search("ab")
    assert pt.search("aba")
    assert pt.search("abab")                                                                                                                                                                                                                
    assert pt.search("caba")
    assert not pt.search("cabacaba")

    assert pt.starts_with("a")
    assert pt.starts_with("ab")
    assert pt.starts_with("aba")
    assert pt.starts_with("abab")
    assert pt.starts_with("caba")
    assert not pt.starts_with("cabacaba")


def test_prefix_tree_augmented_sample():
    """Tests for PrefixTreeAugmented class."""
    pta = PrefixTreeAugmented()
    pta.insert("aba")
    pta.insert("aba")
    pta.insert("aba")
    pta.insert("abab")
    pta.insert("ababad")
    pta.insert("caba")

    # The basic operations should still work correctly.
    assert not pta.search("a")
    assert not pta.search("ab")
    assert pta.search("aba")
    assert pta.search("abab")
    assert pta.search("caba")
    assert not pta.search("cabacaba")

    assert pta.starts_with("a")
    assert pta.starts_with("ab")
    assert pta.starts_with("aba")
    assert pta.starts_with("abab")
    assert pta.starts_with("caba")
    assert not pta.starts_with("cabacaba")

    # The new operations.
    assert pta.count_words_equal_to("aba") == 3
    assert pta.count_words_equal_to("ab") == 0
    assert pta.count_words_equal_to("abab") == 1
    assert pta.count_words_equal_to("cabacaba") == 0

    assert pta.count_words_starting_with("") == 6
    assert pta.count_words_starting_with("a") == 5
    assert pta.count_words_starting_with("ab") == 5
    assert pta.count_words_starting_with("aba") == 5
    assert pta.count_words_starting_with("abab") == 2
    assert pta.count_words_starting_with("ababa") == 1
    assert pta.count_words_starting_with("c") == 1


def test_get_number_of_matches_sample():
    """Tests for get_number_of_matches class."""
    assert get_number_of_matches(
        "abracadabra",
        ["a", "a", "abra", "ca"]
    ) == 13

    assert get_number_of_matches(
        "hello world",
        ["hell", "l", "l", "o"]
    ) == 9

    assert get_number_of_matches(
        "Tomatoes make great weapons when water balloons aren’t available.",
        ["at", "ma", "great weapons"]
    ) == 6
