from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None
    root = TreeNode(values[0], None, None)
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i], None, None)
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i], None, None)
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
    def verticalTraversal(self, root):
        if root is None:
            return []
        node_dict = defaultdict(list)
        min_col = 0
        max_col = 0

        def dfs(node, row, col):
            nonlocal min_col, max_col
            if node is None:
                return
            node_dict[col].append((row, node.val))
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        result = []
        for col in range(min_col, max_col + 1):
            node_dict[col].sort(key=lambda x: (x[0], x[1]))
            result.append([val for _, val in node_dict[col]])
        return result