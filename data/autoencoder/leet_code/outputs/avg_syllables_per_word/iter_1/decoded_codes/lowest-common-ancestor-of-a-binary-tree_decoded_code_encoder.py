from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
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

def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        return left if left is not None else right