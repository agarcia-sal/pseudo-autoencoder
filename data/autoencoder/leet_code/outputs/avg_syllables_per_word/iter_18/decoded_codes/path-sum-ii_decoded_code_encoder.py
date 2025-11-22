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
    index_tracker = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if index_tracker < len(values) and values[index_tracker] is not None:
            node.left = TreeNode(values[index_tracker])
            queue.append(node.left)
        index_tracker += 1
        if index_tracker < len(values) and values[index_tracker] is not None:
            node.right = TreeNode(values[index_tracker])
            queue.append(node.right)
        index_tracker += 1
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node: Optional[TreeNode], current_sum: int, path: List[int]):
            if node is None:
                return
            path.append(node.val)
            current_sum += node.val
            if node.left is None and node.right is None and current_sum == targetSum:
                result.append(path[:])
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            path.pop()
        dfs(root, 0, [])
        return result