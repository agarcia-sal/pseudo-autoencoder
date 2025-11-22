from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values_list: List[Optional[int]]) -> Optional[TreeNode]:
    if not values_list:
        return None
    root = TreeNode(values_list[0])
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values_list) and values_list[i] is not None:
            node.left = TreeNode(values_list[i])
            queue.append(node.left)
        i += 1
        if i < len(values_list) and values_list[i] is not None:
            node.right = TreeNode(values_list[i])
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p_node: Optional[TreeNode], q_node: Optional[TreeNode]) -> bool:
    if p_node is None and q_node is None:
        return True
    elif p_node is None or q_node is None:
        return False
    elif p_node.val != q_node.val:
        return False
    else:
        return is_same_tree(p_node.left, q_node.left) and is_same_tree(p_node.right, q_node.right)

class Solution:
    def tree2str(self, root_node: Optional[TreeNode]) -> str:
        def helper(node: Optional[TreeNode]) -> str:
            if node is None:
                return ""
            result = str(node.val)
            if node.left is not None or node.right is not None:
                result += "(" + helper(node.left) + ")"
            if node.right is not None:
                result += "(" + helper(node.right) + ")"
            return result
        return helper(root_node)