from collections import deque
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values):
            left_val = values[i]
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            i += 1
        if i < len(values):
            right_val = values[i]
            if right_val is not None:
                node.right = TreeNode(right_val)
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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_len = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal max_len
            if node is None:
                return 0, 0
            inc_len, dec_len = 1, 1
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            if node.left:
                if node.val == node.left.val + 1:
                    dec_len = left_dec + 1
                elif node.val == node.left.val - 1:
                    inc_len = left_inc + 1
            if node.right:
                if node.val == node.right.val + 1:
                    dec_len = max(dec_len, right_dec + 1)
                elif node.val == node.right.val - 1:
                    inc_len = max(inc_len, right_inc + 1)
            max_len = max(max_len, inc_len + dec_len - 1)
            return inc_len, dec_len

        dfs(root)
        return max_len