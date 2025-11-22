from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    index_pointer = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if index_pointer < len(values) and values[index_pointer] is not None:
            node.left = TreeNode(values[index_pointer])
            queue.append(node.left)
        index_pointer += 1
        if index_pointer < len(values) and values[index_pointer] is not None:
            node.right = TreeNode(values[index_pointer])
            queue.append(node.right)
        index_pointer += 1
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            node.left = None
            if stack:
                node.right = stack[-1]
            else:
                node.right = None