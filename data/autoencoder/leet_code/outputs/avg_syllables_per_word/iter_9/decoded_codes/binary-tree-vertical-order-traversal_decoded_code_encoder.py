from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val, left=None, right=None):
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
    def verticalOrder(self, root):
        if root is None:
            return []
        column_table = defaultdict(list)
        queue = deque([(root, 0)])
        min_column = max_column = 0
        while queue:
            node, col = queue.popleft()
            if node:
                column_table[col].append(node.val)
                min_column = min(min_column, col)
                max_column = max(max_column, col)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        return [column_table[x] for x in range(min_column, max_column + 1)]