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
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
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
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return None, 0
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_node, left_depth + 1
            if right_depth > left_depth:
                return right_node, right_depth + 1
            return node, left_depth + 1
        return dfs(root)[0]