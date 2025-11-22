from collections import deque, defaultdict
from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        node_dict: defaultdict[int, List[Tuple[int, int]]] = defaultdict(list)
        min_col = 0
        max_col = 0

        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            nonlocal min_col, max_col
            if node is None:
                return
            node_dict[col].append((row, node.val))
            if col < min_col:
                min_col = col
            if col > max_col:
                max_col = col
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result: List[List[int]] = []
        for col in range(min_col, max_col + 1):
            # Sort by row, then value
            sorted_list = sorted(node_dict[col], key=lambda x: (x[0], x[1]))
            column_values = [val for _, val in sorted_list]
            result.append(column_values)

        return result