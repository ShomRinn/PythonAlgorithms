"""Templates for programming assignments: Huffman coding."""


from collections import Counter
from string import ascii_lowercase


class TreeNode:
    """Class that represents nodes that would be used to create a Huffman coding.
    
    NOTE: you may augment this class if needed (i.e., add some methods or attributes); however,
    the initial constructor should still work.
    """

    def __init__(self, character: str = None, left: "TreeNode" = None, right: "TreeNode" = None):
        self.character = character
        self.left = left
        self.right = right


def create_huffman_coding(text: str) -> TreeNode:
    frequency = Counter(text)
    nodes = sorted([(freq, TreeNode(character=char)) for char, freq in frequency.items()],
                   key=lambda x: (-x[0], x[1].character))

    while len(nodes) > 1:
        (freq1, node1), (freq2, node2) = nodes[-2], nodes[-1]
        nodes = nodes[:-2]

        merged_node = TreeNode(character=node1.character + node2.character, left=node1, right=node2)

        nodes.append((freq1 + freq2, merged_node))
        nodes = sorted(nodes, key=lambda x: (-x[0], x[1].character))

    return nodes[0][1]

def encode_huffman(text: str, huffman_coding_root: TreeNode) -> str:
    """Returns an encoded message using Huffman coding for a given text.

    NOTE: `text` consists of `string.ascii_lowercase` symbols only.

    Args:
        text: str, a given text to encode
        huffman_coding_root: TreeNode, the root node that represents a given Huffman coding
    Returns:
        str, the encoded text
    """
    d = {}

    stack = [(huffman_coding_root, '')]
    while stack:
        e, code = stack.pop()

        if e.left:
            stack.append((e.left, code + '0'))
            stack.append((e.right, code + '1'))
        else:
            d[e.character] = code

    if len(d) == 1:
        for k in d:
            d[k] = '0'

    output = ''.join([d[char] for char in text])
    return output

def decode_huffman(text: str, huffman_coding_root: TreeNode) -> str:
    """Uses Huffman coding to return the decoded message for a given text.

    NOTE: `text` consists of `string.ascii_lowercase` symbols only.

    Args:
        text: str, a given text to decode
        huffman_coding_root: TreeNode, the root node that represents a given Huffman coding
    Returns:
        str, the decoded text
    """
    d = {}

    stack = [(huffman_coding_root, '')]
    while stack:
        e, code = stack.pop()

        if e.left:
            stack.append((e.left, code + '0'))
            stack.append((e.right, code + '1'))
        else:
            d[code] = e.character

    if len(d) == 1:
        value = d['']
        del d['']
        d['0'] = value
    output = ''
    while text != '':
        for k in d:
            if text.startswith(k):
                output += d[k]
                text = text[len(k):]

    return output
