from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(list_of_values: List[Optional[int]]) -> Optional[TreeNode]:
    if not list_of_values:
        return None
    root = TreeNode(list_of_values[0])
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.left = TreeNode(list_of_values[i])
            queue.append(node.left)
        i += 1
        if i < len(list_of_values) and list_of_values[i] is not None:
            node.right = TreeNode(list_of_values[i])
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
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        from collections import deque

        result = deque()

        def inorder_traversal(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder_traversal(node.left)
            if len(result) < k:
                result.append(node.val)
            else:
                if abs(node.val - target) < abs(result[0] - target):
                    result.popleft()
                    result.append(node.val)
                else:
                    return
            inorder_traversal(node.right)

        inorder_traversal(root)
        return list(result)