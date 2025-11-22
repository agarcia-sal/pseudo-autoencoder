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
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def findLeaves(self, root):
        result = []
        def collectLeaves(node):
            if not node:
                return -1
            lh = collectLeaves(node.left)
            rh = collectLeaves(node.right)
            h = max(lh, rh) + 1
            if h >= len(result):
                result.append([])
            result[h].append(node.val)
            return h
        collectLeaves(root)
        return result