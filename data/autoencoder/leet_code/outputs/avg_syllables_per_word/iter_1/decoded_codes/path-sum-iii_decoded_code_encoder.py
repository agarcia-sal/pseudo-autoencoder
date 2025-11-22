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
    queue = deque([root])
    i = 1
    while queue and i < len(values):
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
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def pathSum(self, root, targetSum):
        def helper(node, cur_sum, prefix_sums):
            if not node:
                return 0
            cur_sum += node.val
            paths = prefix_sums.get(cur_sum - targetSum, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
            paths += helper(node.left, cur_sum, prefix_sums)
            paths += helper(node.right, cur_sum, prefix_sums)
            prefix_sums[cur_sum] -= 1
            return paths
        return helper(root, 0, {0:1})