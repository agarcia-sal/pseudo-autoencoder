from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if len(values) == 0:
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(node: Optional[TreeNode]) -> str:
            if node is None:
                return ""
            result = str(node.val)
            # Include left subtree if it exists, or if left is None but right is not None (need "()")
            if node.left is not None or (node.left is None and node.right is not None):
                result += "(" + helper(node.left) + ")"
            if node.right is not None:
                result += "(" + helper(node.right) + ")"
            return result
        return helper(root)