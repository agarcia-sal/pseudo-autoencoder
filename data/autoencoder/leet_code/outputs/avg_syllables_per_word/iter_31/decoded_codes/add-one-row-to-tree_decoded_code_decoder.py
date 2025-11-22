from collections import deque
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0], None, None)
    i = 1
    queue = deque([root])
    while queue and i < len(values):
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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        queue: deque[Tuple[TreeNode, int]] = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if level == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
            elif level < depth - 1:
                if node.left is not None:
                    queue.append((node.left, level + 1))
                if node.right is not None:
                    queue.append((node.right, level + 1))
        return root