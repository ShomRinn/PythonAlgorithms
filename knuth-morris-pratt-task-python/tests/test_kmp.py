"""Sample tests for 'tasks.kmp' module."""
from tasks.kmp import build_lps_array, find_occurrences_via_kmp, is_tandem_repeat


def test_build_lps_array_sample():
    """Tests for build_lps_array function."""
    assert build_lps_array("abracadabra") == [0, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4]
    assert build_lps_array("abacaba") == [0, 0, 1, 0, 1, 2, 3]
    assert build_lps_array("ababbaab") == [0, 0, 1, 2, 0, 1, 1, 2]


def test_find_occurrences_via_kmp_sample():
    """Tests for find_occurrences_via_kmp function."""
    assert find_occurrences_via_kmp("hello world", "o") == [4, 7]
    assert find_occurrences_via_kmp("abacaba", "aba") == [0, 4]
    assert find_occurrences_via_kmp("ababbaab", "ab") == [0, 2, 6]


def test_is_tandem_repeat_sample():
    """Tests for is_tandem_repeat function."""
    assert is_tandem_repeat("abacaba") == False
    assert is_tandem_repeat("abaabaabaaba") == True
    assert is_tandem_repeat("ababab") == True
    assert is_tandem_repeat("a") == False
