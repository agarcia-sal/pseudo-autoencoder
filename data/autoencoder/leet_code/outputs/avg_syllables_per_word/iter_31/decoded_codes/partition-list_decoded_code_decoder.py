from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def list_node(values: list[int]) -> Optional[ListNode]:
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
    while p1 is not None and p2 is not None:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return p1 is None and p2 is None


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less = less_head
        greater = greater_head
        current = head

        while current is not None:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        greater.next = None
        less.next = greater_head.next
        return less_head.next