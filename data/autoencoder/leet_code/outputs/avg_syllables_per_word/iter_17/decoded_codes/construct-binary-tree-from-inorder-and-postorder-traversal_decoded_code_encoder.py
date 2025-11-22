from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(list_of_values: List[Optional[int]]) -> Optional[TreeNode]:
    if not list_of_values:
        return None
    root = TreeNode(list_of_values[0])
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.left = TreeNode(list_of_values[i])
            queue.append(node.left)
        i += 1
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.right = TreeNode(list_of_values[i])
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def buildTree(self, inorder_list: List[int], postorder_list: List[int]) -> Optional[TreeNode]:
        if not inorder_list or not postorder_list:
            return None
        root_val = postorder_list.pop()
        root = TreeNode(root_val)
        root_index = inorder_list.index(root_val)
        # Build right subtree before left subtree because postorder root is at the end
        root.right = self.buildTree(inorder_list[root_index + 1:], postorder_list)
        root.left = self.buildTree(inorder_list[:root_index], postorder_list)
        return root