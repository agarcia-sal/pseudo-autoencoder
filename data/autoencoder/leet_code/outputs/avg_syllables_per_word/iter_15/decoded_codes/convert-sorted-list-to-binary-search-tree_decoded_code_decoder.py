from collections import deque
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(values: list) -> Optional[ListNode]:
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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: list) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque()
    queue.append(root)
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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None

        def findMiddle(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
            slow = left
            fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def convertListToBST(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[TreeNode]:
            if left == right:
                return None

            mid = findMiddle(left, right)
            node = TreeNode(mid.val)
            node.left = convertListToBST(left, mid)
            node.right = convertListToBST(mid.next, right)
            return node

        return convertListToBST(head, None)