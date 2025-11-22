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
    iterator_index = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if iterator_index < len(values) and values[iterator_index] is not None:
            node.left = TreeNode(values[iterator_index])
            queue.append(node.left)
        iterator_index += 1
        if iterator_index < len(values) and values[iterator_index] is not None:
            node.right = TreeNode(values[iterator_index])
            queue.append(node.right)
        iterator_index += 1
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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        height = getHeight(root)
        width = (2 ** height) - 1
        res = [["" for _ in range(width)] for _ in range(height)]

        def placeNode(node: Optional[TreeNode], row: int, left: int, right: int) -> None:
            if node is None:
                return
            middle_position = (left + right) // 2
            res[row][middle_position] = str(node.val)
            placeNode(node.left, row + 1, left, middle_position)
            placeNode(node.right, row + 1, middle_position + 1, right)

        placeNode(root, 0, 0, width)
        return res