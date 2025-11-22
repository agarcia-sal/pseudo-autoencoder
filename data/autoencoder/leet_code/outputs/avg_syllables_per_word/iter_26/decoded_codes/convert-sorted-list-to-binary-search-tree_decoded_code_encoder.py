from collections import deque
from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def list_node(values_list: List[int]) -> Optional[ListNode]:
    if not values_list:
        return None
    head = ListNode(values_list[0])
    p = head
    for value in values_list[1:]:
        node = ListNode(value)
        p.next = node
        p = node
    return head

def is_same_list(pointer_one: Optional[ListNode], pointer_two: Optional[ListNode]) -> bool:
    if pointer_one is None and pointer_two is None:
        return True
    if pointer_one is None or pointer_two is None:
        return False
    return (pointer_one.val == pointer_two.val and
            is_same_list(pointer_one.next, pointer_two.next))

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values_list: List[Optional[int]]) -> Optional[TreeNode]:
    if not values_list:
        return None
    root = TreeNode(values_list[0])
    index = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if index < len(values_list) and values_list[index] is not None:
            node.left = TreeNode(values_list[index])
            queue.append(node.left)
        index += 1
        if index < len(values_list) and values_list[index] is not None:
            node.right = TreeNode(values_list[index])
            queue.append(node.right)
        index += 1
    return root

def is_same_tree(pointer_p: Optional[TreeNode], pointer_q: Optional[TreeNode]) -> bool:
    if pointer_p is None and pointer_q is None:
        return True
    if pointer_p is None or pointer_q is None:
        return False
    if pointer_p.val != pointer_q.val:
        return False
    return (is_same_tree(pointer_p.left, pointer_q.left) and
            is_same_tree(pointer_p.right, pointer_q.right))

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