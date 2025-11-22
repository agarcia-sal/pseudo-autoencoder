from collections import deque
from typing import Optional, List, Tuple

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

def is_same_tree(tree_node_p: Optional[TreeNode], tree_node_q: Optional[TreeNode]) -> bool:
    if tree_node_p is None and tree_node_q is None:
        return True
    if tree_node_p is None or tree_node_q is None:
        return False
    if tree_node_p.val != tree_node_q.val:
        return False
    return (is_same_tree(tree_node_p.left, tree_node_q.left) and 
            is_same_tree(tree_node_p.right, tree_node_q.right))

class Solution:
    def rob(self, root_node: Optional[TreeNode]) -> int:
        def rob_from_node(current_node: Optional[TreeNode]) -> Tuple[int, int]:
            if current_node is None:
                return 0, 0
            left_robbed, left_not_robbed = rob_from_node(current_node.left)
            right_robbed, right_not_robbed = rob_from_node(current_node.right)
            rob_this_node = current_node.val + left_not_robbed + right_not_robbed
            not_rob_this_node = max(left_robbed, left_not_robbed) + max(right_robbed, right_not_robbed)
            return rob_this_node, not_rob_this_node
        return max(rob_from_node(root_node))