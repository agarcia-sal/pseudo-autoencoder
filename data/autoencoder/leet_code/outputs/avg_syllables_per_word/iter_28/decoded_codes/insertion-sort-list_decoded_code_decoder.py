from typing import Optional, Iterable


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def list_node(values: Iterable[int]) -> Optional[ListNode]:
    values = list(values)
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


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(-5001)
        dummy.next = head
        current = head.next
        head.next = None
        while current:
            next_node = current.next
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = next_node
        return dummy.next