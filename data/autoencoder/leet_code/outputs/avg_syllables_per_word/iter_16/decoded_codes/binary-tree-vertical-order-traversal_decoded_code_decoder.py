from collections import deque, defaultdict
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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        column_table = defaultdict(list)
        queue = deque([(root, 0)])
        min_column = 0
        max_column = 0
        while queue:
            node, column_index = queue.popleft()
            if node is not None:
                column_table[column_index].append(node.val)
                if column_index < min_column:
                    min_column = column_index
                if column_index > max_column:
                    max_column = column_index
                queue.append((node.left, column_index - 1))
                queue.append((node.right, column_index + 1))
        return [column_table[x] for x in range(min_column, max_column + 1)]