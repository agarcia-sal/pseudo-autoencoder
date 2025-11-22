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
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        def is_leaf(n):
            return not n.left and not n.right

        left_b = []
        c = root.left
        while c:
            if not is_leaf(c):
                left_b.append(c.val)
            c = c.left if c.left else c.right

        right_b = []
        c = root.right
        while c:
            if not is_leaf(c):
                right_b.append(c.val)
            c = c.right if c.right else c.left

        leaves = []
        def collect_leaves(n):
            if not n:
                return
            if is_leaf(n):
                leaves.append(n.val)
            collect_leaves(n.left)
            collect_leaves(n.right)

        collect_leaves(root)
        if is_leaf(root):
            leaves = []

        return [root.val] + left_b + leaves + right_b[::-1]