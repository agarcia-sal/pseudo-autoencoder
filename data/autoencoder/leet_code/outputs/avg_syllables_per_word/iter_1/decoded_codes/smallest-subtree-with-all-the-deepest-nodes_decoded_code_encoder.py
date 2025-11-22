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
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def subtreeWithAllDeepest(self, root):
        def dfs(n):
            if n is None:
                return None, 0
            Ln, Ld = dfs(n.left)
            Rn, Rd = dfs(n.right)
            if Ld > Rd:
                return Ln, Ld + 1
            if Rd > Ld:
                return Rn, Rd + 1
            return n, Ld + 1
        return dfs(root)[0]