from collections import deque
from typing import Optional, Tuple, List, Union

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: Union[List[Optional[int]], None]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0], None, None)
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i], None, None)
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[int]]:
            if node is None:
                return 0, None
            left_len, left_val = dfs(node.left)
            right_len, right_val = dfs(node.right)
            left_arrow = right_arrow = 0
            if node.left is not None and node.left.val == node.val:
                left_arrow = left_len + 1
            if node.right is not None and node.right.val == node.val:
                right_arrow = right_len + 1
            self.max_length = max(self.max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow), node.val

        self.max_length = 0
        dfs(root)
        return self.max_length