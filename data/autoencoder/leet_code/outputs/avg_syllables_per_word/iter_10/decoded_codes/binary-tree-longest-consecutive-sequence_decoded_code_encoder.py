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
    def longestConsecutive(self, root):
        if not root:
            return 0
        def dfs(node, parent_val, length):
            if not node:
                return length
            length = length + 1 if parent_val is not None and node.val == parent_val + 1 else 1
            left_len = dfs(node.left, node.val, length)
            right_len = dfs(node.right, node.val, length)
            return max(length, left_len, right_len)
        return dfs(root, None, 0)