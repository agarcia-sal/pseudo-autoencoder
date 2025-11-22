from collections import deque, defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
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
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        queue = deque([(root, 0)])
        min_column = 0
        max_column = 0

        while queue:
            node, column_index = queue.popleft()
            if node:
                column_table[column_index].append(node.val)
                min_column = min(min_column, column_index)
                max_column = max(max_column, column_index)

                queue.append((node.left, column_index - 1))
                queue.append((node.right, column_index + 1))

        return [column_table[col] for col in range(min_column, max_column + 1)]