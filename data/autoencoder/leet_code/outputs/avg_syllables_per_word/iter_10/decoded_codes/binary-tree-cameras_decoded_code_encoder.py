from collections import deque
from math import inf

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

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def minCameraCover(self, root):
        def dfs(node):
            if node is None:
                return 0, 0, inf
            left_no_cam, left_monitored, left_cam = dfs(node.left)
            right_no_cam, right_monitored, right_cam = dfs(node.right)

            no_camera = left_monitored + right_monitored
            monitored = min(
                left_cam + min(right_monitored, right_cam),
                right_cam + min(left_monitored, left_cam),
                left_cam + right_cam
            )
            camera = 1 + min(left_no_cam, left_monitored, left_cam) + min(right_no_cam, right_monitored, right_cam)

            return no_camera, monitored, camera

        _, monitored, camera = dfs(root)
        return min(monitored, camera)