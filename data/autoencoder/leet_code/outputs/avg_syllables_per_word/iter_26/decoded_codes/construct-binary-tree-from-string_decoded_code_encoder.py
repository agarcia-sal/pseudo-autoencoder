from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(list_of_values):
    if not list_of_values:
        return None
    head = ListNode(list_of_values[0])
    p = head
    for value in list_of_values[1:]:
        node = ListNode(value)
        p.next = node
        p = node
    return head

def is_same_list(p1, p2):
    if p1 is None and p2 is None:
        return True
    if p1 is None or p2 is None:
        return False
    return (p1.val == p2.val) and is_same_list(p1.next, p2.next)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(list_of_values):
    if not list_of_values:
        return None
    root = TreeNode(list_of_values[0])
    i = 1
    queue = deque([root])
    n = len(list_of_values)
    while queue:
        node = queue.popleft()
        if i < n and list_of_values[i] is not None:
            node.left = TreeNode(list_of_values[i])
            queue.append(node.left)
        i += 1
        if i < n and list_of_values[i] is not None:
            node.right = TreeNode(list_of_values[i])
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
    def str2tree(self, s):
        def parse_tree(index):
            if index >= len(s):
                return None, index

            start = index
            # includes '-' for negative numbers
            while index < len(s) and (s[index].isdigit() or s[index] == '-'):
                index += 1

            node_val = int(s[start:index])
            node = TreeNode(node_val)

            if index < len(s) and s[index] == '(':
                node.left, index = parse_tree(index + 1)

            if index < len(s) and s[index] == '(':
                node.right, index = parse_tree(index + 1)

            if index < len(s) and s[index] == ')':
                index += 1

            return node, index

        root, _ = parse_tree(0)
        return root