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
            l_no, l_mon, l_cam = dfs(node.left)
            r_no, r_mon, r_cam = dfs(node.right)

            no_camera = l_mon + r_mon

            monitored = min(
                l_cam + min(r_mon, r_cam),
                r_cam + min(l_mon, l_cam),
                l_cam + r_cam,
            )

            camera = 1 + min(l_no, l_mon, l_cam) + min(r_no, r_mon, r_cam)

            return no_camera, monitored, camera

        root_no, root_mon, root_cam = dfs(root)
        return min(root_mon, root_cam)