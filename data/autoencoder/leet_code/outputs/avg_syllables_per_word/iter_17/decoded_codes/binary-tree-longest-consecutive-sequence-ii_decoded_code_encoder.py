from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(list_of_values):
    if not list_of_values:
        return None
    root = TreeNode(list_of_values[0])
    i = 1
    queue = deque([root])
    while queue and i < len(list_of_values):
        node = queue.popleft()
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.left = TreeNode(list_of_values[i])
            queue.append(node.left)
        i += 1
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.right = TreeNode(list_of_values[i])
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(node_p, node_q):
    if node_p is None and node_q is None:
        return True
    if node_p is None or node_q is None:
        return False
    if node_p.val != node_q.val:
        return False
    return is_same_tree(node_p.left, node_q.left) and is_same_tree(node_p.right, node_q.right)

class Solution:
    def longestConsecutive(self, root):
        self.max_len = 0

        def dfs(node):
            if node is None:
                return 0, 0
            inc_len = dec_len = 1
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)

            if node.left:
                if node.val == node.left.val + 1:
                    dec_len = left_dec + 1
                elif node.val == node.left.val - 1:
                    inc_len = left_inc + 1
            if node.right:
                if node.val == node.right.val + 1:
                    dec_len = max(dec_len, right_dec + 1)
                elif node.val == node.right.val - 1:
                    inc_len = max(inc_len, right_inc + 1)

            self.max_len = max(self.max_len, inc_len + dec_len - 1)
            return inc_len, dec_len

        dfs(root)
        return self.max_len