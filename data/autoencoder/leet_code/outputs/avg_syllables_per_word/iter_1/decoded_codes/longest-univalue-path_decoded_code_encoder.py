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
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
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
    def longestUnivaluePath(self, root):
        max_len = 0
        def dfs(node):
            nonlocal max_len
            if not node:
                return 0, 0
            l_len, l_val = dfs(node.left)
            r_len, r_val = dfs(node.right)
            l_arrow = r_arrow = 0
            if node.left and node.left.val == node.val:
                l_arrow = l_len + 1
            if node.right and node.right.val == node.val:
                r_arrow = r_len + 1
            max_len = max(max_len, l_arrow + r_arrow)
            return max(l_arrow, r_arrow), node.val
        dfs(root)
        return max_len