from collections import deque, defaultdict

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

def is_same_tree(node_p, node_q):
    if node_p is None and node_q is None:
        return True
    if node_p is None or node_q is None:
        return False
    if node_p.val != node_q.val:
        return False
    return is_same_tree(node_p.left, node_q.left) and is_same_tree(node_p.right, node_q.right)

class Solution:
    def findFrequentTreeSum(self, root_node):
        count = defaultdict(int)
        def subtree_sum(node):
            if node is None:
                return 0
            current_sum = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            count[current_sum] += 1
            return current_sum
        subtree_sum(root_node)
        max_freq = max(count.values(), default=0)
        return [k for k, v in count.items() if v == max_freq]