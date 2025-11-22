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
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def findClosestLeaf(self, root, k):
        if not root.left and not root.right:
            return root.val
        graph = defaultdict(list)
        def dfs(node, parent=None):
            if parent is not None:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        dfs(root)
        queue = deque([k])
        visited = set()
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if len(graph[current]) == 1 and current != root.val:
                return current
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return -1