from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(list_of_values):
    if not list_of_values:
        return None
    root_node = TreeNode(list_of_values[0])
    index_counter = 1
    node_queue = deque([root_node])
    while node_queue:
        current_node = node_queue.popleft()
        if index_counter < len(list_of_values) and list_of_values[index_counter] is not None:
            left_child = TreeNode(list_of_values[index_counter])
            current_node.left = left_child
            node_queue.append(left_child)
        index_counter += 1
        if index_counter < len(list_of_values) and list_of_values[index_counter] is not None:
            right_child = TreeNode(list_of_values[index_counter])
            current_node.right = right_child
            node_queue.append(right_child)
        index_counter += 1
    return root_node

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
    def pathSum(self, root, targetSum):
        def helper(node, current_sum, prefix_sums):
            if node is None:
                return 0
            current_sum += node.val
            needed_sum = current_sum - targetSum
            paths_to_here = prefix_sums.get(needed_sum, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            paths_in_left = helper(node.left, current_sum, prefix_sums)
            paths_in_right = helper(node.right, current_sum, prefix_sums)
            prefix_sums[current_sum] -= 1
            if prefix_sums[current_sum] == 0:
                del prefix_sums[current_sum]
            return paths_to_here + paths_in_left + paths_in_right

        initial_prefix_sums = {0: 1}
        return helper(root, 0, initial_prefix_sums)