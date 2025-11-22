from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        prev = None
        curr = root

        while curr:
            if curr.left is None:
                if prev is not None and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right is not None and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev is not None and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        if first is not None and second is not None:
            # Swap values without extra space
            first.val = first.val + second.val
            second.val = first.val - second.val
            first.val = first.val - second.val