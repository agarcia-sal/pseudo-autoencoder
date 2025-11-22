from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(list_of_values: List[Optional[int]]) -> Optional[TreeNode]:
    if not list_of_values:
        return None
    root = TreeNode(list_of_values[0])
    index = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if index < len(list_of_values) and list_of_values[index] is not None:
            node.left = TreeNode(list_of_values[index])
            queue.append(node.left)
        index += 1
        if index < len(list_of_values) and list_of_values[index] is not None:
            node.right = TreeNode(list_of_values[index])
            queue.append(node.right)
        index += 1
    return root

def is_same_tree(p_node: Optional[TreeNode], q_node: Optional[TreeNode]) -> bool:
    if p_node is None and q_node is None:
        return True
    if p_node is None or q_node is None:
        return False
    if p_node.val != q_node.val:
        return False
    return is_same_tree(p_node.left, q_node.left) and is_same_tree(p_node.right, q_node.right)

class Solution:
    def kthSmallest(self, root_node: Optional[TreeNode], k_value: int) -> int:
        stack_structure = []
        current_node = root_node
        count_tracker = 0
        while stack_structure or current_node is not None:
            while current_node is not None:
                stack_structure.append(current_node)
                current_node = current_node.left
            current_node = stack_structure.pop()
            count_tracker += 1
            if count_tracker == k_value:
                return current_node.val
            current_node = current_node.right