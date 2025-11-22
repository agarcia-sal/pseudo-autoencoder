from collections import deque
from typing import Optional, List, Any


class TreeNode:
    def __init__(self, val: Any, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: List[Optional[Any]]) -> Optional[TreeNode]:
    if len(values) == 0:
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode],
                     low: Optional[Any] = float('-inf'),
                     high: Optional[Any] = float('inf')) -> bool:
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)