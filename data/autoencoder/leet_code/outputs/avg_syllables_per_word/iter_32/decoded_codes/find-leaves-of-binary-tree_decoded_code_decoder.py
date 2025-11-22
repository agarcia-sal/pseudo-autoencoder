from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def collectLeaves(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            left_height = collectLeaves(node.left)
            right_height = collectLeaves(node.right)
            current_height = max(left_height, right_height) + 1
            if current_height >= len(result):
                result.append([])
            result[current_height].append(node.val)
            return current_height

        collectLeaves(root)
        return result