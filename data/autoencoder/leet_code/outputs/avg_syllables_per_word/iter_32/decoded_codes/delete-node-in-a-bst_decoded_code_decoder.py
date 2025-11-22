from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0], None, None)
    queue = deque([root])
    i = 1
    n = len(values)

    while queue:
        node = queue.popleft()
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i], None, None)
            queue.append(node.left)
        i += 1

        if i < n and values[i] is not None:
            node.right = TreeNode(values[i], None, None)
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # root.val == key, delete this node
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Node with two children: find the smallest node in right subtree
        node = root.right
        while node.left:
            node = node.left

        # Attach left subtree of the root to the left of successor node
        node.left = root.left

        # Return root.right as new root
        return root.right