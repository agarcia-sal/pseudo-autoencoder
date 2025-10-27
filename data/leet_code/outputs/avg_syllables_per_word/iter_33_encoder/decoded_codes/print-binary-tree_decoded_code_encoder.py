from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
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
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        height = getHeight(root)
        width = (1 << height) - 1  # 2^height - 1
        res = [["" for _ in range(width)] for _ in range(height)]

        def placeNode(node: Optional[TreeNode], row: int, left: int, right: int):
            if node is None:
                return
            mid = (left + right) // 2
            res[row][mid] = str(node.val)
            placeNode(node.left, row + 1, left, mid)
            placeNode(node.right, row + 1, mid + 1, right)

        placeNode(root, 0, 0, width)
        return res