"""Sample tests for 'tasks.huffman' module."""
from tasks.huffman import create_huffman_coding, encode_huffman, decode_huffman, TreeNode


def test_create_huffman_coding_sample():
    """Tests for create_huffman_coding function."""
    # Example 1
    root = create_huffman_coding("cabbaa")
    assert root.left.character == "a"
    assert root.right.left.character == "b"
    assert root.right.right.character == "c"

    # Example 2
    root = create_huffman_coding("aaaabbbbccdd")
    assert root.right.character == "a"
    assert root.left.left.character == "b"
    assert root.left.right.left.character == "c"    
    assert root.left.right.right.character == "d"    

    # Example 3
    root = create_huffman_coding("abcabdedeea")
    assert root.left.left.character == "a"
    assert root.left.right.left.character == "d"
    assert root.left.right.right.character == "c"
    assert root.right.left.character == "e"
    assert root.right.right.character == "b"

    # Example 4
    root = create_huffman_coding("aaaa")
    assert root.character == "a"


def test_encode_huffman_sample():
    """Tests for encode_huffman function."""
    # Example 1
    root = TreeNode(left=TreeNode("a"), right=TreeNode(left=TreeNode("b"), right=TreeNode("c")))
    assert encode_huffman("abacaba", root) == "0100110100"

    # Example 2
    root = TreeNode(
        left=TreeNode(
            left=TreeNode("b"),
            right=TreeNode(left=TreeNode("c"), right=TreeNode("d"))
        ),
        right=TreeNode("a")
    )
    assert encode_huffman("abacaba", root) == "10010101001"

    # Example 3
    root = TreeNode(
        left=TreeNode(
            left=TreeNode("a"),
            right=TreeNode(left=TreeNode("d"), right=TreeNode("c"))
        ),
        right=TreeNode(left=TreeNode("e"), right=TreeNode("b"))
    )  
    assert encode_huffman("abacaba", root) == "001100011001100"

    # Example 4
    root = TreeNode("a")
    assert encode_huffman("aaaa", root) == "0000"


def test_decode_huffman_sample():
    """Tests for decode_huffman function."""
    # Example 1
    root = TreeNode(left=TreeNode("a"), right=TreeNode(left=TreeNode("b"), right=TreeNode("c")))
    assert decode_huffman("0100110100", root) == "abacaba"

    # Example 2
    root = TreeNode(
        left=TreeNode(
            left=TreeNode("b"),
            right=TreeNode(left=TreeNode("c"), right=TreeNode("d"))
        ),
        right=TreeNode("a")
    )
    assert decode_huffman("10010101001", root) == "abacaba"

    # Example 3
    root = TreeNode(
        left=TreeNode(
            left=TreeNode("a"),
            right=TreeNode(left=TreeNode("d"), right=TreeNode("c"))
        ),
        right=TreeNode(left=TreeNode("e"), right=TreeNode("b"))
    )  
    assert decode_huffman("001100011001100", root) == "abacaba"

    # Example 4
    root = TreeNode("a")
    assert decode_huffman("0000", root) == "aaaa"
