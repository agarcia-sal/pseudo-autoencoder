from collections import defaultdict, deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
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
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
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
            # A leaf node in the graph has exactly one neighbor except for the root
            if len(graph[current]) == 1 and current != root.val:
                return current
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return -1