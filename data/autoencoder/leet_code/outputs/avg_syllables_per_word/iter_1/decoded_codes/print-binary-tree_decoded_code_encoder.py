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
    def printTree(self, root):
        def getHeight(n):
            if not n:
                return 0
            return 1 + max(getHeight(n.left), getHeight(n.right))

        h = getHeight(root)
        w = 2**h - 1
        res = [[""] * w for _ in range(h)]

        def placeNode(n, r, L, R):
            if not n:
                return
            m = (L + R) // 2
            res[r][m] = str(n.val)
            placeNode(n.left, r + 1, L, m)
            placeNode(n.right, r + 1, m + 1, R)

        placeNode(root, 0, 0, w)
        return res