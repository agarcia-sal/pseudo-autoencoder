from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque()
    queue.append(root)
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
    def verticalOrder(self, root):
        if root is None:
            return []
        column_table = defaultdict(list)
        queue = deque([(root, 0)])
        min_column = 0
        max_column = 0
        while queue:
            node, column_index = queue.popleft()
            if node is not None:
                column_table[column_index].append(node.val)
                min_column = min(min_column, column_index)
                max_column = max(max_column, column_index)
                queue.append((node.left, column_index - 1))
                queue.append((node.right, column_index + 1))
        result = []
        for x in range(min_column, max_column + 1):
            result.append(column_table[x])
        return result