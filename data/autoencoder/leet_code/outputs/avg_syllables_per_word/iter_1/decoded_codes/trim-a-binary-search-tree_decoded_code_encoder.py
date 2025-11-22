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
    def trimBST(self, root, low, high):
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root