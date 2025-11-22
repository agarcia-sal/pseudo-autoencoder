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
    i = 1
    q = deque([root])
    while q and i < len(vals):
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
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    @staticmethod
    def checkEqualTree(root):
        def subtree_sum(n):
            if not n:
                return 0
            return n.val + subtree_sum(n.left) + subtree_sum(n.right)

        total = subtree_sum(root)
        if total % 2 != 0:
            return False
        target = total // 2
        found = [False]

        def can_split(n):
            if not n:
                return 0
            s = n.val + can_split(n.left) + can_split(n.right)
            if s == target and n != root:
                found[0] = True
            return s

        can_split(root)
        return found[0]