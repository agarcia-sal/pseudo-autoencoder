from collections import deque
from math import inf
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int, int]:
            # Returns a tuple (no_camera, monitored, camera)
            if node is None:
                return 0, 0, inf
            left_no_cam, left_monitored, left_camera = dfs(node.left)
            right_no_cam, right_monitored, right_camera = dfs(node.right)

            no_camera = left_monitored + right_monitored

            monitored = min(
                left_camera + min(right_monitored, right_camera),
                right_camera + min(left_monitored, left_camera),
                left_camera + right_camera,
            )

            camera = 1 + min(left_no_cam, left_monitored, left_camera) + min(right_no_cam, right_monitored, right_camera)

            return no_camera, monitored, camera

        root_no_camera, root_monitored, root_camera = dfs(root)
        return min(root_monitored, root_camera)