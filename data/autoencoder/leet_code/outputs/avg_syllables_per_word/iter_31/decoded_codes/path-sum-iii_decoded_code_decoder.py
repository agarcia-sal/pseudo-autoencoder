from collections import deque
from typing import Optional, List, Dict

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node: Optional[TreeNode], current_sum: int, prefix_sums: Dict[int, int]) -> int:
            if node is None:
                return 0
            current_sum += node.val
            paths_to_here = prefix_sums.get(current_sum - targetSum, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            paths_in_left = helper(node.left, current_sum, prefix_sums)
            paths_in_right = helper(node.right, current_sum, prefix_sums)
            prefix_sums[current_sum] -= 1
            return paths_to_here + paths_in_left + paths_in_right

        prefix_sums = {0: 1}
        return helper(root, 0, prefix_sums)