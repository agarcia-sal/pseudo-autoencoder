from collections import deque, defaultdict

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
    def verticalTraversal(self, root):
        if not root:
            return []
        node_dict = defaultdict(list)
        min_col, max_col = 0, 0

        def dfs(node, row, col):
            nonlocal min_col, max_col
            if not node:
                return
            node_dict[col].append((row, node.val))
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in range(min_col, max_col + 1):
            sorted_list = sorted(node_dict[col], key=lambda x: (x[0], x[1]))
            result.append([val for _, val in sorted_list])
        return result