from collections import deque
from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if len(values) == 0:
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
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue: deque[Tuple[TreeNode, int]] = deque([(root, 0)])
        max_width = 0
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                if i == level_length - 1:
                    width = index - first_index + 1
                    if width > max_width:
                        max_width = width
                if node.left is not None:
                    queue.append((node.left, 2 * index))
                if node.right is not None:
                    queue.append((node.right, 2 * index + 1))
        return max_width