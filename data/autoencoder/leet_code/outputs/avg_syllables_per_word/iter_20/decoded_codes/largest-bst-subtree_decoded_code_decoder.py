from collections import deque
from math import inf
from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
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
        if i < len(values):
            lv = values[i]
            if lv is not None:
                node.left = TreeNode(lv)
                queue.append(node.left)
            i += 1
        if i < len(values):
            rv = values[i]
            if rv is not None:
                node.right = TreeNode(rv)
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
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int, int]:
            if node is None:
                return inf, -inf, 0

            left_min, left_max, left_size = dfs(node.left)
            right_min, right_max, right_size = dfs(node.right)

            if left_max < node.val < right_min:
                cur_min = min(left_min, node.val)
                cur_max = max(right_max, node.val)
                cur_size = left_size + right_size + 1
                return cur_min, cur_max, cur_size

            return -inf, inf, max(left_size, right_size)

        return dfs(root)[2]