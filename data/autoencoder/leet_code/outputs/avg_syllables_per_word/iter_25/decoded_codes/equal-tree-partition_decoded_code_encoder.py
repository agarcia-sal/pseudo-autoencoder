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
    def checkEqualTree(self, root):
        def subtree_sum(node):
            if node is None:
                return 0
            return node.val + subtree_sum(node.left) + subtree_sum(node.right)

        total_sum = subtree_sum(root)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        found = [False]

        def can_split(node):
            if node is None:
                return 0
            current_sum = node.val + can_split(node.left) + can_split(node.right)
            if current_sum == target and node is not root:
                found[0] = True
            return current_sum

        can_split(root)
        return found[0]