from collections import deque, defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
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

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        if root.left is None and root.right is None:
            return root.val

        graph = defaultdict(list)

        def dfs(node: TreeNode, parent: Optional[TreeNode] = None):
            if parent is not None:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left is not None:
                dfs(node.left, node)
            if node.right is not None:
                dfs(node.right, node)

        dfs(root)
        queue = deque([k])
        visited = set()
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            # A leaf is a node whose adjacency list length is 1 and it is not root, or node has no neighbors (single node tree)
            # To make sure that we correctly detect leaf nodes in all cases:
            # Since edges are undirected, leaves have exactly one neighbor except the root might also have one neighbor if root is leaf
            # The problem states root can be leaf if no children - handled initially
            # So here leaf iff len(graph[current]) == 1
            if len(graph[current]) == 1 and current != root.val:
                return current
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return -1