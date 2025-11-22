from collections import deque
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if values is None or len(values) == 0:
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def rob_from_node(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0

            left_robbed, left_not_robbed = rob_from_node(node.left)
            right_robbed, right_not_robbed = rob_from_node(node.right)

            rob_this_node = node.val + left_not_robbed + right_not_robbed
            not_rob_this_node = max(left_robbed, left_not_robbed) + max(right_robbed, right_not_robbed)

            return rob_this_node, not_rob_this_node

        return max(rob_from_node(root))