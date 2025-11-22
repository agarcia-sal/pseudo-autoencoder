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
    index_counter = 1
    node_queue = deque([root])
    while node_queue:
        current_node = node_queue.popleft()
        if index_counter < len(values) and values[index_counter] is not None:
            current_node.left = TreeNode(values[index_counter])
            node_queue.append(current_node.left)
        index_counter += 1
        if index_counter < len(values) and values[index_counter] is not None:
            current_node.right = TreeNode(values[index_counter])
            node_queue.append(current_node.right)
        index_counter += 1
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        node_queue = deque([root])
        left_to_right = True
        while node_queue:
            level_size = len(node_queue)
            current_level = deque()
            for _ in range(level_size):
                current_node = node_queue.popleft()
                if left_to_right:
                    current_level.append(current_node.val)
                else:
                    current_level.appendleft(current_node.val)
                if current_node.left is not None:
                    node_queue.append(current_node.left)
                if current_node.right is not None:
                    node_queue.append(current_node.right)
            result.append(list(current_level))
            left_to_right = not left_to_right
        return result