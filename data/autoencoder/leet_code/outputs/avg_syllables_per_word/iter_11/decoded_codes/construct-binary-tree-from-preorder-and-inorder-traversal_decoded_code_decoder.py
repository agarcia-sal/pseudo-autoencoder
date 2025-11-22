from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
    if values is None or len(values) == 0:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque([root])
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None or len(preorder) == 0 or inorder is None or len(inorder) == 0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index_inorder = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:1+root_index_inorder], inorder[:root_index_inorder])
        root.right = self.buildTree(preorder[1+root_index_inorder:], inorder[root_index_inorder+1:])
        return root