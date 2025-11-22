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
    def pathSum(self, root, targetSum):
        result = []
        def dfs(node, current_sum, path):
            if not node:
                return
            path.append(node.val)
            current_sum += node.val
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path[:])
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            path.pop()
        dfs(root, 0, [])
        return result