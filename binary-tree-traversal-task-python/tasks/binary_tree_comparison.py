"""Templates for programming assignments: binary trees comparison."""

from typing import Optional

from tasks.binary_tree_node import TreeNode


def check_trees_equality(p_tree: Optional[TreeNode], q_tree: Optional[TreeNode]) -> bool:
    if not p_tree and not q_tree:
        return True
    if not p_tree or not q_tree or p_tree.value != q_tree.value:
        return False
    return check_trees_equality(p_tree.left, q_tree.left) and check_trees_equality(p_tree.right, q_tree.right)

