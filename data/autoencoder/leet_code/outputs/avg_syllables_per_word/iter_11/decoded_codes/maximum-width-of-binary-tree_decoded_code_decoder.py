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
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        queue = deque([(root, 0)])
        max_width = 0
        while queue:
            level_length = len(queue)
            first_index = queue[0][1]
            for position in range(level_length):
                node, index = queue.popleft()
                if position == level_length - 1:
                    width = index - first_index + 1
                    if max_width < width:
                        max_width = width
                if node.left is not None:
                    queue.append((node.left, index * 2))
                if node.right is not None:
                    queue.append((node.right, index * 2 + 1))
        return max_width