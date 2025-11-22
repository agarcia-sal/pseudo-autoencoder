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
    i = 1
    q = deque([root])
    while q:
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
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
    def closestKValues(self, root, target, k):
        result = deque()

        def inorder_traversal(node):
            if node is None:
                return
            inorder_traversal(node.left)

            if len(result) < k:
                result.append(node.val)
            elif abs(node.val - target) < abs(result[0] - target):
                result.popleft()
                result.append(node.val)
            else:
                return

            inorder_traversal(node.right)

        inorder_traversal(root)
        return list(result)