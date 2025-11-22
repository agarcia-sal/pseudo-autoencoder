from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None
    root = TreeNode(values[0], None, None)
    i = 1
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i], None, None)
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i], None, None)
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def largestBSTSubtree(self, root):
        def dfs(node):
            if node is None:
                return inf, -inf, 0
            left_min, left_max, left_size = dfs(node.left)
            right_min, right_max, right_size = dfs(node.right)
            if left_max < node.val < right_min:
                return min(node.val, left_min), max(node.val, right_max), left_size + right_size + 1
            return -inf, inf, max(left_size, right_size)
        return dfs(root)[2]