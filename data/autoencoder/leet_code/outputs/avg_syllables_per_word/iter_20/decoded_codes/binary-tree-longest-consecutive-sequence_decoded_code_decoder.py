from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values):
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
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node: Optional[TreeNode], parent_val: Optional[int], current_length: int) -> int:
            if node is None:
                return current_length

            if parent_val is not None and node.val == parent_val + 1:
                current_length += 1
            else:
                current_length = 1

            left_length = dfs(node.left, node.val, current_length)
            right_length = dfs(node.right, node.val, current_length)

            return max(current_length, left_length, right_length)

        return dfs(root, None, 0)