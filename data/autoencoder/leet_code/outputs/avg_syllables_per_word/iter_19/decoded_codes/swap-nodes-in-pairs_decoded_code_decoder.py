from typing import Optional

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def list_node(values):
    if not values:
        return None
    head = ListNode(values[0], None)
    p = head
    for val in values[1:]:
        node = ListNode(val, None)
        p.next = node
        p = node
    return head

def is_same_list(p1, p2):
    if p1 is None and p2 is None:
        return True
    if p1 is None or p2 is None:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, None)
        dummy.next = head
        current = dummy
        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next
            current.next = second
            first.next = second.next
            second.next = first
            current = first.next
        return dummy.next