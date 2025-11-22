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
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        ltr = True
        while q:
            sz = len(q)
            lvl = deque()
            for _ in range(sz):
                n = q.popleft()
                if ltr:
                    lvl.append(n.val)
                else:
                    lvl.appendleft(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(list(lvl))
            ltr = not ltr
        return res