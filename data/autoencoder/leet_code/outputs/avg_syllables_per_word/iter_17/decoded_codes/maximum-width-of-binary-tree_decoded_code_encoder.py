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
    root_node = TreeNode(list_of_values[0])
    i = 1
    queue = deque([root_node])
    while queue and i < len(list_of_values):
        node = queue.popleft()
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.left = TreeNode(list_of_values[i])
            queue.append(node.left)
        i += 1
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.right = TreeNode(list_of_values[i])
            queue.append(node.right)
        i += 1
    return root_node


def is_same_tree(node_p: Optional[TreeNode], node_q: Optional[TreeNode]) -> bool:
    if node_p is None and node_q is None:
        return True
    if node_p is None or node_q is None:
        return False
    if node_p.val != node_q.val:
        return False
    return is_same_tree(node_p.left, node_q.left) and is_same_tree(node_p.right, node_q.right)


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root, 0)])
        max_width = 0
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                if i == level_length - 1:
                    width = index - first_index + 1
                    if max_width < width:
                        max_width = width
                if node.left is not None:
                    queue.append((node.left, 2 * index))
                if node.right is not None:
                    queue.append((node.right, 2 * index + 1))
        return max_width