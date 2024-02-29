"""Templates for programming assignments: binary search tree operations."""

from typing import Optional

from tasks.binary_tree_node import TreeNode


def search_in_bst(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.value == value:
        return root
    elif value < root.value:
        return search_in_bst(root.left, value)
    else:
        return search_in_bst(root.right, value)



def insert_in_bst(root: Optional[TreeNode], value: int) -> TreeNode:
    if not root:
        return TreeNode(value)

    if value < root.value:
        root.left = insert_in_bst(root.left, value)
    else:
        root.right = insert_in_bst(root.right, value)

    return root

