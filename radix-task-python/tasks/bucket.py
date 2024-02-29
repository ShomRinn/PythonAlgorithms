"""Template for programming assignment: the bucket sort algorithm."""
from typing import List, Tuple


def bucket_sort(patterns: List[str], prefix_length: int) -> List[Tuple[int, int]]:
    """Orders a given array of strings using bucket sort.

    NOTE: for bucketing purposes, you need to use the first `prefix_length` characters of each input pattern.
    Example 1: 
    | patterns = ["aa", "ab", "ba", "bb", "bbac"], prefix_length=1
    | buckets = {"a": ["aa", "ab"], "b": ["ba", "bb", "bbac"]}

    Example 2: 
    | patterns = ["aa", "ab", "ba", "bb", "bbac"], prefix_length=2
    | There will be four buckets (two patterns in the bucket "bb").

    NOTE: for each input pattern, you should return two things:
    * the final positions of patterns after bucket sort
    * the positions of patterns in corresponding buckets after ordering within buckets
    
    Args:
        patterns: List[str], a given list of patterns to order
        prefix_length: int, a parameter that should be used to bucket patterns
    Returns:
        List[Tuple[int, int]], positions that correspond to given patterns both globally and 
            within individual buckets
    """
    buckets = {}
    for i, pattern in enumerate(patterns):
        prefix = pattern[:prefix_length]
        if prefix in buckets:
            buckets[prefix].append((pattern, i))
        else:
            buckets[prefix] = [(pattern, i)]

    for prefix in buckets:
        buckets[prefix].sort(key=lambda x: x[0])

    result = []
    global_pos = 0
    for prefix in sorted(buckets.keys()):
        for local_pos, (pattern, original_index) in enumerate(buckets[prefix]):
            result.append((original_index, (global_pos, local_pos)))
            global_pos += 1

    result.sort(key=lambda x: x[0])
    return [pos for _, pos in result]