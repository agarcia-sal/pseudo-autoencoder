from collections import deque
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)

    while queue and i < n:
        node = queue.popleft()
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < n and values[i] is not None:
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_width = 0
        queue: deque[Tuple[TreeNode, int]] = deque([(root, 0)])

        while queue:
            level_length = len(queue)
            first_index = queue[0][1]
            for i in range(level_length):
                node, index = queue.popleft()
                # Normalize index to prevent integer overflow and keep numbers manageable
                cur_index = index - first_index
                if i == level_length - 1:
                    width = cur_index + 1
                    if width > max_width:
                        max_width = width
                if node.left is not None:
                    queue.append((node.left, 2 * cur_index))
                if node.right is not None:
                    queue.append((node.right, 2 * cur_index + 1))

        return max_width