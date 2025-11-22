from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    index_tracker = 1
    node_queue = deque([root])
    while node_queue:
        current_node = node_queue.popleft()
        if index_tracker < len(values) and values[index_tracker] is not None:
            current_node.left = TreeNode(values[index_tracker])
            node_queue.append(current_node.left)
        index_tracker += 1
        if index_tracker < len(values) and values[index_tracker] is not None:
            current_node.right = TreeNode(values[index_tracker])
            node_queue.append(current_node.right)
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        node_queue = deque([root])
        while node_queue:
            level_size = len(node_queue)
            current_level = []
            for _ in range(level_size):
                current_node = node_queue.popleft()
                current_level.append(current_node.val)
                if current_node.left is not None:
                    node_queue.append(current_node.left)
                if current_node.right is not None:
                    node_queue.append(current_node.right)
            result.append(current_level)
        return result