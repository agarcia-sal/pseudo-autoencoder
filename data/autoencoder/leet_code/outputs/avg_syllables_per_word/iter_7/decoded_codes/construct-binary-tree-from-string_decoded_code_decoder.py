from collections import deque
from typing import Optional, List, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val = val
        self.next = next


def list_node(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    p = head
    for val in values[1:]:
        node = ListNode(val)
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
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
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
            # parse number including optional '-'
            if s[index] == '-':
                index += 1
            while index < len(s) and s[index].isdigit():
                index += 1
            val = int(s[start:index])
            node = TreeNode(val)

            if index < len(s) and s[index] == '(':
                node.left, index = parse_tree(index + 1)
            if index < len(s) and s[index] == '(':
                node.right, index = parse_tree(index + 1)
            if index < len(s) and s[index] == ')':
                index += 1
            return node, index

        root, _ = parse_tree(0)
        return root