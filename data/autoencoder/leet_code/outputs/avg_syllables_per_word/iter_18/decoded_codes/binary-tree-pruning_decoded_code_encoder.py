from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None
    root = TreeNode(values[0])
    index_counter = 1
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        if index_counter < len(values) and values[index_counter] is not None:
            current_node.left = TreeNode(values[index_counter])
            queue.append(current_node.left)
        index_counter += 1
        if index_counter < len(values) and values[index_counter] is not None:
            current_node.right = TreeNode(values[index_counter])
            queue.append(current_node.right)
        index_counter += 1
    return root

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def pruneTree(self, root):
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root