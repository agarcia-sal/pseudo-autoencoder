from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
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
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def countUnivalSubtrees(self, root):
        def helper(n):
            if n is None:
                return (True, 0)
            l_uni, l_cnt = helper(n.left)
            r_uni, r_cnt = helper(n.right)
            if l_uni and r_uni and (n.left is None or n.left.val == n.val) and (n.right is None or n.right.val == n.val):
                return (True, l_cnt + r_cnt + 1)
            return (False, l_cnt + r_cnt)
        _, total = helper(root)
        return total