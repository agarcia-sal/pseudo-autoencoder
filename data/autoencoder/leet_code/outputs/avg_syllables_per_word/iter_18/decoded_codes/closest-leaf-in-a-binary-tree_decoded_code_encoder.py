from collections import deque, defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    index = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
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

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode] = None):
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
            visited.add(current)
            # Leaf check: leaf node has only one neighbor except for the root (which might also have one neighbor)
            if len(graph[current]) == 1 and current != root.val:
                return current
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return -1