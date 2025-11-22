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
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def longestUnivaluePath(self, root):
        def dfs(node):
            if node is None:
                return 0, 0  # length, value
            left_length, left_value = dfs(node.left)
            right_length, right_value = dfs(node.right)
            left_arrow = right_arrow = 0
            if node.left is not None and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right is not None and node.right.val == node.val:
                right_arrow = right_length + 1
            self.max_length = max(self.max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow), node.val

        self.max_length = 0
        dfs(root)
        return self.max_length