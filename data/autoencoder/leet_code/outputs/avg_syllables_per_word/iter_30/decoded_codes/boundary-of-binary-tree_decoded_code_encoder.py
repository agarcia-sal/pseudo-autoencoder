from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        left_boundary = []
        current = root.left
        while current:
            if not is_leaf(current):
                left_boundary.append(current.val)
            if current.left is not None:
                current = current.left
            else:
                current = current.right

        right_boundary = []
        current = root.right
        while current:
            if not is_leaf(current):
                right_boundary.append(current.val)
            if current.right is not None:
                current = current.right
            else:
                current = current.left

        leaves = []

        def collect_leaves(node: Optional[TreeNode]):
            if node is None:
                return
            if is_leaf(node):
                leaves.append(node.val)
            else:
                collect_leaves(node.left)
                collect_leaves(node.right)

        collect_leaves(root)

        if is_leaf(root):
            leaves = []

        return [root.val] + left_boundary + leaves + right_boundary[::-1]