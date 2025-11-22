from collections import deque, defaultdict

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
    def findFrequentTreeSum(self, root):
        count = defaultdict(int)
        def subtree_sum(node):
            if node is None:
                return 0
            current_sum = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            count[current_sum] += 1
            return current_sum
        subtree_sum(root)
        max_freq = max(count.values(), default=0)
        result = [key for key, freq in count.items() if freq == max_freq]
        return result