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
    def longestUnivaluePath(self, root):
        self.max_length = 0

        def dfs(node):
            if node is None:
                return 0, 0
            left_length, left_value = dfs(node.left)
            right_length, right_value = dfs(node.right)

            left_arrow = left_length + 1 if node.left and node.left.val == node.val else 0
            right_arrow = right_length + 1 if node.right and node.right.val == node.val else 0

            self.max_length = max(self.max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow), node.val

        dfs(root)
        return self.max_length