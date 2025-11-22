from collections import deque
from math import inf

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
    def minCameraCover(self, root):
        def dfs(node):
            if not node:
                return (0, 0, inf)  # no_cam, monitored, cam
            L = dfs(node.left)
            R = dfs(node.right)
            no_cam = L[1] + R[1]
            monitored = min(L[2] + min(R[1], R[2]),
                            R[2] + min(L[1], L[2]),
                            L[2] + R[2])
            cam = 1 + min(L) + min(R)
            return (no_cam, monitored, cam)

        res = dfs(root)
        return min(res[1], res[2])