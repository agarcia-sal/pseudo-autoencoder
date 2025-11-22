from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
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

def is_same_tree(node_p: Optional[TreeNode], node_q: Optional[TreeNode]) -> bool:
    if node_p is None and node_q is None:
        return True
    elif node_p is None or node_q is None:
        return False
    elif node_p.val != node_q.val:
        return False
    else:
        return is_same_tree(node_p.left, node_q.left) and is_same_tree(node_p.right, node_q.right)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        node = root.right
        while node.left is not None:
            node = node.left
        node.left = root.left
        root = root.right
        return root