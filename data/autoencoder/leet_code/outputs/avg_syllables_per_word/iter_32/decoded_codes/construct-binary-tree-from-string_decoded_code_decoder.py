from collections import deque
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val: int, next: Optional['ListNode']) -> None:
        self.val = val
        self.next = next


def list_node(values: list[int]) -> Optional[ListNode]:
    if len(values) == 0:
        return None
    head = ListNode(values[0], None)
    p = head
    for val in values[1:]:
        node = ListNode(val, None)
        p.next = node
        p = node
    return head


def is_same_list(p1: Optional[ListNode], p2: Optional[ListNode]) -> bool:
    if p1 is None and p2 is None:
        return True
    if p1 is None or p2 is None:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)


class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'], right: Optional['TreeNode']) -> None:
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: list[Optional[int]]) -> Optional[TreeNode]:
    if len(values) == 0:
        return None
    root = TreeNode(values[0], None, None)
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i], None, None)
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i], None, None)
            queue.append(node.right)
        i += 1
    return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def parse_tree(index: int) -> Tuple[Optional[TreeNode], int]:
            if index >= len(s):
                return None, index

            start = index
            # Parse the integer value which may start with '-'
            if s[index] == '-':
                index += 1
            while index < len(s) and s[index].isdigit():
                index += 1

            # Extract integer string and convert
            val_str = s[start:index]
            if not val_str or val_str == '-':
                # No valid integer found
                return None, index
            node_val = int(val_str)
            node = TreeNode(node_val, None, None)

            # Parse left subtree if present
            if index < len(s) and s[index] == '(':
                node.left, index = parse_tree(index + 1)

            # Parse right subtree if present
            if index < len(s) and s[index] == '(':
                node.right, index = parse_tree(index + 1)

            # Skip closing parenthesis if present
            if index < len(s) and s[index] == ')':
                index += 1

            return node, index

        root, _ = parse_tree(0)
        return root