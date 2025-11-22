from collections import deque
from typing import Optional, List, Union

class TreeNode:
    def __init__(self, val: Union[int, float], left: Optional['TreeNode'], right: Optional['TreeNode']):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[Union[int, float]]]) -> Optional[TreeNode]:
    if len(values) == 0:
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
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> Union[int, float, None]:
        queue = deque([root])
        leftmost_value = None
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    leftmost_value = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return leftmost_value