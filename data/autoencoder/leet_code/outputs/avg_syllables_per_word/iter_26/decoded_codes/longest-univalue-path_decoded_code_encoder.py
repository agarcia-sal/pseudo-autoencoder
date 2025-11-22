from collections import deque
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(list_of_values):
    if not list_of_values:
        return None
    root_node = TreeNode(list_of_values[0])
    index_counter = 1
    node_queue = deque([root_node])
    while node_queue:
        current_node = node_queue.popleft()
        if index_counter < len(list_of_values) and list_of_values[index_counter] is not None:
            current_node.left = TreeNode(list_of_values[index_counter])
            node_queue.append(current_node.left)
        index_counter += 1
        if index_counter < len(list_of_values) and list_of_values[index_counter] is not None:
            current_node.right = TreeNode(list_of_values[index_counter])
            node_queue.append(current_node.right)
        index_counter += 1
    return root_node


def is_same_tree(p_node, q_node):
    if p_node is None and q_node is None:
        return True
    elif p_node is None or q_node is None:
        return False
    elif p_node.val != q_node.val:
        return False
    else:
        return is_same_tree(p_node.left, q_node.left) and is_same_tree(p_node.right, q_node.right)


class Solution:
    def longestUnivaluePath(self, root_node: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[int]]:
            if node is None:
                return 0, None
            left_length, left_value = dfs(node.left)
            right_length, right_value = dfs(node.right)

            left_arrow = 0
            if node.left is not None and node.left.val == node.val:
                left_arrow = left_length + 1

            right_arrow = 0
            if node.right is not None and node.right.val == node.val:
                right_arrow = right_length + 1

            self.max_length = max(self.max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow), node.val

        self.max_length = 0
        dfs(root_node)
        return self.max_length