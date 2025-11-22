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
    index = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
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
        node_dict = defaultdict(list)
        min_col = 0
        max_col = 0

        # Use nonlocal to allow modification in nested scope
        def dfs(node: Optional[TreeNode], row: int, col: int):
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

        result = []
        for col in range(min_col, max_col + 1):
            sorted_list = sorted(node_dict[col], key=lambda x: (x[0], x[1]))
            result.append([val for _, val in sorted_list])
        return result