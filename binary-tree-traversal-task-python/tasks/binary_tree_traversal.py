"""Templates for programming assignments: binary tree traversal methods."""

from typing import List, Optional

from tasks.binary_tree_node import TreeNode


def get_inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    def inorder(node):
        return inorder(node.left) + [node.value] + inorder(node.right) if node else []
    return inorder(root)



def get_postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    def postorder(node):
        return postorder(node.left) + postorder(node.right) + [node.value] if node else []
    return postorder(root)



def get_preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    def preorder(node):
        return [node.value] + preorder(node.left) + preorder(node.right) if node else []
    return preorder(root)



def get_level_order_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    queue, result = [root], []
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

