from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if len(values) == 0:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque()
    queue.append(root)
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
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def longestConsecutive(self, root):
        self.max_len = 0

        def dfs(node):
            if node is None:
                return 0, 0
            inc_len, dec_len = 1, 1
            left_inc, left_dec = 0, 0
            right_inc, right_dec = 0, 0

            if node.left is not None:
                left_inc, left_dec = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec_len = left_dec + 1
                elif node.val == node.left.val - 1:
                    inc_len = left_inc + 1

            if node.right is not None:
                right_inc, right_dec = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec_len = max(dec_len, right_dec + 1)
                elif node.val == node.right.val - 1:
                    inc_len = max(inc_len, right_inc + 1)

            self.max_len = max(self.max_len, inc_len + dec_len - 1)
            return inc_len, dec_len

        dfs(root)
        return self.max_len