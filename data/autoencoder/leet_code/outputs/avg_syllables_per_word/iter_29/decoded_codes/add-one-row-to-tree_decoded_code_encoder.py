from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values_list: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
    if not values_list:
        return None
    root_node = TreeNode(values_list[0])
    i = 1
    queue_structure = deque([root_node])
    while queue_structure:
        node = queue_structure.popleft()
        if i < len(values_list) and values_list[i] is not None:
            node.left = TreeNode(values_list[i])
            queue_structure.append(node.left)
        i += 1
        if i < len(values_list) and values_list[i] is not None:
            node.right = TreeNode(values_list[i])
            queue_structure.append(node.right)
        i += 1
    return root_node

def is_same_tree(first_tree_node: Optional[TreeNode], second_tree_node: Optional[TreeNode]) -> bool:
    if first_tree_node is None and second_tree_node is None:
        return True
    elif first_tree_node is None or second_tree_node is None:
        return False
    elif first_tree_node.val != second_tree_node.val:
        return False
    else:
        return (is_same_tree(first_tree_node.left, second_tree_node.left) and
                is_same_tree(first_tree_node.right, second_tree_node.right))

class Solution:
    def addOneRow(self, root_tree_node: Optional[TreeNode], val_to_add: int, depth_level: int) -> Optional[TreeNode]:
        if depth_level == 1:
            return TreeNode(val_to_add, left=root_tree_node)
        queue_structure = deque([(root_tree_node, 1)])
        while queue_structure:
            node, current_level = queue_structure.popleft()
            if current_level == depth_level - 1:
                node.left = TreeNode(val_to_add, left=node.left)
                node.right = TreeNode(val_to_add, right=node.right)
            elif current_level < depth_level - 1:
                if node.left is not None:
                    queue_structure.append((node.left, current_level + 1))
                if node.right is not None:
                    queue_structure.append((node.right, current_level + 1))
        return root_tree_node