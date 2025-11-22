from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
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

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def maxPathSum(self, root):
        def helper(node):
            if node is None:
                return -inf, -inf
            left_max, left_gain = helper(node.left)
            right_max, right_gain = helper(node.right)
            current_max = node.val + max(left_gain, 0) + max(right_gain, 0)
            current_gain = node.val + max(max(left_gain, right_gain), 0)
            global_max = max(left_max, right_max, current_max)
            return global_max, current_gain
        return helper(root)[0]