from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values_list):
    if not values_list:
        return None
    root = TreeNode(values_list[0])
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values_list) and values_list[i] is not None:
            node.left = TreeNode(values_list[i])
            queue.append(node.left)
        i += 1
        if i < len(values_list) and values_list[i] is not None:
            node.right = TreeNode(values_list[i])
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
    def closestKValues(self, root, target_value, k):
        result = deque()

        def inorder_traversal(node):
            if node is None:
                return
            inorder_traversal(node.left)
            if len(result) < k:
                result.append(node.val)
            else:
                if abs(node.val - target_value) < abs(result[0] - target_value):
                    result.popleft()
                    result.append(node.val)
                else:
                    return
            inorder_traversal(node.right)

        inorder_traversal(root)
        return list(result)