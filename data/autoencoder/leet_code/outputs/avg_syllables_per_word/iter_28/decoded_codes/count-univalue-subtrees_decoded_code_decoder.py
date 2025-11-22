from collections import deque
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: list) -> Optional[TreeNode]:
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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if node is None:
                return True, 0
            is_left_unival, left_count = helper(node.left)
            is_right_unival, right_count = helper(node.right)
            if is_left_unival and is_right_unival:
                if (node.left is None or node.left.val == node.val) and \
                   (node.right is None or node.right.val == node.val):
                    return True, left_count + right_count + 1
            return False, left_count + right_count

        _, count = helper(root)
        return count