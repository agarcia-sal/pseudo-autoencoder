from typing import Optional, List

class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None):
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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n + 1):
            if first is None:
                raise IndexError("n is larger than the length of the list")
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        to_remove = second.next
        if to_remove is not None:
            second.next = to_remove.next
        else:
            # If to_remove is None, n is invalid (too large), raise an error
            raise IndexError("n is larger than the length of the list")
        return dummy.next