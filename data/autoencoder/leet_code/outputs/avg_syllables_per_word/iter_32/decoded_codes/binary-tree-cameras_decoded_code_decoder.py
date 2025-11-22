from collections import deque
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']) -> None:
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: list) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0], None, None)
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i], None, None)
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i], None, None)
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
        from math import inf

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int, int]:
            if node is None:
                # no_camera=0 (subtree covered with no camera on current node),
                # monitored=0 (subtree covered but current node monitored without camera),
                # camera=inf (can't put camera at None)
                return 0, 0, inf
            left_no_camera, left_monitored, left_camera = dfs(node.left)
            right_no_camera, right_monitored, right_camera = dfs(node.right)

            no_camera = left_monitored + right_monitored

            # Monitored but no camera at current node:
            # Either left or right has camera covering this node
            monitored = min(
                left_camera + min(right_monitored, right_camera),
                right_camera + min(left_monitored, left_camera),
                left_camera + right_camera,
            )

            camera = 1 + min(left_no_camera, left_monitored, left_camera) + min(right_no_camera, right_monitored, right_camera)

            return no_camera, monitored, camera

        root_no_camera, root_monitored, root_camera = dfs(root)
        return min(root_monitored, root_camera)