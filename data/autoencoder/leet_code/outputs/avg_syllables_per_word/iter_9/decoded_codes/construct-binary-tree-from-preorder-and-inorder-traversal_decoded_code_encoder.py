from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
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
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index_inorder = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:1+root_index_inorder], inorder[:root_index_inorder])
        root.right = self.buildTree(preorder[1+root_index_inorder:], inorder[root_index_inorder+1:])
        return root