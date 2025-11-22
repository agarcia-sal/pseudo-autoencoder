from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values_list: List[Optional[int]]) -> Optional[TreeNode]:
    if not values_list:
        return None
    root = TreeNode(values_list[0])
    index_counter = 1
    queue_collection = deque([root])
    while queue_collection:
        node = queue_collection.popleft()
        if index_counter < len(values_list) and values_list[index_counter] is not None:
            node.left = TreeNode(values_list[index_counter])
            queue_collection.append(node.left)
        index_counter += 1
        if index_counter < len(values_list) and values_list[index_counter] is not None:
            node.right = TreeNode(values_list[index_counter])
            queue_collection.append(node.right)
        index_counter += 1
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        stack_collection = [root]
        while stack_collection:
            node = stack_collection.pop()
            if node.right:
                stack_collection.append(node.right)
            if node.left:
                stack_collection.append(node.left)
            node.left = None
            node.right = stack_collection[-1] if stack_collection else None