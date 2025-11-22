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
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def longestConsecutive(self, root):
        max_len = 0

        def dfs(node):
            nonlocal max_len
            if node is None:
                return 0, 0
            inc_len = dec_len = 1
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            if node.left is not None:
                if node.val == node.left.val + 1:
                    dec_len = left_dec + 1
                elif node.val == node.left.val - 1:
                    inc_len = left_inc + 1
            if node.right is not None:
                if node.val == node.right.val + 1:
                    dec_len = max(dec_len, right_dec + 1)
                elif node.val == node.right.val - 1:
                    inc_len = max(inc_len, right_inc + 1)
            max_len = max(max_len, inc_len + dec_len - 1)
            return inc_len, dec_len

        dfs(root)
        return max_len