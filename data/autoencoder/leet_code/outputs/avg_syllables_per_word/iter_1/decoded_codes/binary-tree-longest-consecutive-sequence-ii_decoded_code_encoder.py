from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q:
        n = q.popleft()
        if i < len(vals) and vals[i] is not None:
            n.left = TreeNode(vals[i])
            q.append(n.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            n.right = TreeNode(vals[i])
            q.append(n.right)
        i += 1
    return root

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def longestConsecutive(self, root):
        max_len = 0

        def dfs(node):
            nonlocal max_len
            if not node:
                return (0, 0)
            inc = dec = 1
            l_inc, l_dec = dfs(node.left)
            r_inc, r_dec = dfs(node.right)
            if node.left:
                if node.val == node.left.val + 1:
                    dec = l_dec + 1
                elif node.val == node.left.val - 1:
                    inc = l_inc + 1
            if node.right:
                if node.val == node.right.val + 1:
                    dec = max(dec, r_dec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, r_inc + 1)
            max_len = max(max_len, inc + dec - 1)
            return (inc, dec)

        dfs(root)
        return max_len