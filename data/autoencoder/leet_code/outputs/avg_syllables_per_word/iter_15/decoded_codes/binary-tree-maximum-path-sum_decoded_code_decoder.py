from collections import deque
from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque([root])
    while queue:
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]) -> Tuple[float, float]:
            if node is None:
                return float('-inf'), float('-inf')
            left_max, left_gain = helper(node.left)
            right_max, right_gain = helper(node.right)
            current_max = node.val + max(left_gain, 0) + max(right_gain, 0)
            current_gain = node.val + max(left_gain, right_gain, 0)
            global_max = max(left_max, right_max, current_max)
            return global_max, current_gain
        return helper(root)[0]