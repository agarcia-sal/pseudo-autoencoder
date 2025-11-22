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
    queue = deque([root])
    i = 1
    while queue:
        n = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            n.left = TreeNode(vals[i])
            queue.append(n.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            n.right = TreeNode(vals[i])
            queue.append(n.right)
        i += 1
    return root

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def recoverTree(self, root):
        first = second = prev = None
        curr = root
        while curr:
            if not curr.left:
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right
        if first and second:
            first.val, second.val = second.val, first.val