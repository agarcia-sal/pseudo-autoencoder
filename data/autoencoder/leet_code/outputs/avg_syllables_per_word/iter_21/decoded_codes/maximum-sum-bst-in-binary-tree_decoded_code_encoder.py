from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if values is None:
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
    def maxSumBST(self, root):
        self.max_sum = 0

        def helper(node):
            if node is None:
                return True, 0, inf, -inf
            left_is_bst, left_sum, left_min, left_max = helper(node.left)
            right_is_bst, right_sum, right_min, right_max = helper(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_sum = left_sum + right_sum + node.val
                current_min = min(node.val, left_min)
                current_max = max(node.val, right_max)
                self.max_sum = max(self.max_sum, current_sum)
                return True, current_sum, current_min, current_max
            return False, 0, inf, -inf

        helper(root)
        return self.max_sum