from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(list_of_values: List[Optional[int]]) -> Optional[TreeNode]:
    if not list_of_values:
        return None
    root = TreeNode(list_of_values[0])
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.left = TreeNode(list_of_values[i])
            queue.append(node.left)
        i += 1
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.right = TreeNode(list_of_values[i])
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], current_sum: int, path: List[int]) -> None:
            if node is None:
                return
            path.append(node.val)
            current_sum += node.val
            if node.left is None and node.right is None and current_sum == targetSum:
                result.append(path[:])  # append a copy of path
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            path.pop()

        result: List[List[int]] = []
        dfs(root, 0, [])
        return result