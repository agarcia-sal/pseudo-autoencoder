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
    q = deque([root])
    while q:
        n = q.popleft()
        if i < len(values) and values[i] is not None:
            n.left = TreeNode(values[i])
            q.append(n.left)
        i += 1
        if i < len(values) and values[i] is not None:
            n.right = TreeNode(values[i])
            q.append(n.right)
        i += 1
    return root

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def maxSumBST(self, root):
        max_sum = 0

        def helper(node):
            nonlocal max_sum
            if not node:
                return True, 0, inf, -inf
            l_bst, l_sum, l_min, l_max = helper(node.left)
            r_bst, r_sum, r_min, r_max = helper(node.right)
            if l_bst and r_bst and l_max < node.val < r_min:
                cur_sum = l_sum + r_sum + node.val
                cur_min = min(node.val, l_min)
                cur_max = max(node.val, r_max)
                max_sum = max(max_sum, cur_sum)
                return True, cur_sum, cur_min, cur_max
            return False, 0, inf, -inf

        helper(root)
        return max_sum