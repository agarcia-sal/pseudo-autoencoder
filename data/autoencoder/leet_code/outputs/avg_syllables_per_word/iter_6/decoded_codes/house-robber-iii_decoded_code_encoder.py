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
    def rob(self, root):
        def rob_from_node(node):
            if not node:
                return 0, 0
            left_robbed, left_not_robbed = rob_from_node(node.left)
            right_robbed, right_not_robbed = rob_from_node(node.right)
            rob_this_node = node.val + left_not_robbed + right_not_robbed
            not_rob_this_node = max(left_robbed, left_not_robbed) + max(right_robbed, right_not_robbed)
            return rob_this_node, not_rob_this_node
        return max(rob_from_node(root))