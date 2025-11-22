from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if len(values) == 0:
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        max_val = max(nums)
        max_index = nums.index(max_val)
        root = TreeNode(max_val)
        # Sublist before max_index
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        # Sublist after max_index
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root