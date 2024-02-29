"""Templates for programming assignments: binary tree properties."""

from typing import Optional

from tasks.binary_tree_node import TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    def check(node):
        if not node:
            return 0, True

        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)

        return height, balanced

    return check(root)[1]



def is_binary_search_tree(root: Optional[TreeNode]) -> bool:
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.value < high):
            return False
        return validate(node.left, low, node.value) and validate(node.right, node.value, high)

    return validate(root)

