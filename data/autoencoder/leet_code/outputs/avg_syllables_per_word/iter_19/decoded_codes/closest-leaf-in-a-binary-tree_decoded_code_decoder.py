import collections
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
    def findClosestLeaf(self, root, k):
        if root.left is None and root.right is None:
            return root.val
        graph = defaultdict(list)
        def dfs(node, parent):
            if parent is not None:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left is not None:
                dfs(node.left, node)
            if node.right is not None:
                dfs(node.right, node)
        dfs(root, None)
        queue = deque([k])
        visited = set()
        while queue:
            current = queue.popleft()
            visited.add(current)
            if len(graph[current]) == 1 and current != root.val:
                return current
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return -1