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
    node_queue = deque([root])
    while node_queue:
        current_node = node_queue.popleft()
        if index_counter < len(values) and values[index_counter] is not None:
            current_node.left = TreeNode(values[index_counter])
            node_queue.append(current_node.left)
        index_counter += 1
        if index_counter < len(values) and values[index_counter] is not None:
            current_node.right = TreeNode(values[index_counter])
            node_queue.append(current_node.right)
        index_counter += 1
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
    def findLeaves(self, root):
        result = []
        def collectLeaves(node):
            if node is None:
                return -1
            left_height = collectLeaves(node.left)
            right_height = collectLeaves(node.right)
            current_height = max(left_height, right_height) + 1
            if current_height >= len(result):
                result.append([])
            result[current_height].append(node.val)
            return current_height

        collectLeaves(root)
        return result