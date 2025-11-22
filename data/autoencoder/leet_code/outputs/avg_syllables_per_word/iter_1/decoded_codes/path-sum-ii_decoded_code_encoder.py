from collections import deque
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
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
        def dfs(node, currSum, path):
            if not node:
                return
            path.append(node.val)
            currSum += node.val
            if not node.left and not node.right and currSum == targetSum:
                result.append(copy.deepcopy(path))
            dfs(node.left, currSum, path)
            dfs(node.right, currSum, path)
            path.pop()
        dfs(root, 0, [])
        return result