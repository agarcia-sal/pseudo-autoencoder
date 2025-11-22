from collections import deque
from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: list) -> Optional[TreeNode]:
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
    if p is None or q is None or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0, inf  # no_camera, monitored, camera
            left_no, left_mon, left_cam = dfs(node.left)
            right_no, right_mon, right_cam = dfs(node.right)

            no_camera = left_mon + right_mon

            monitored = min(
                left_cam + min(right_mon, right_cam),
                right_cam + min(left_mon, left_cam),
                left_cam + right_cam
            )

            camera = 1 + min(left_no, left_mon, left_cam) + min(right_no, right_mon, right_cam)

            return no_camera, monitored, camera

        no_camera, monitored, camera = dfs(root)
        return min(monitored, camera)