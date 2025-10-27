from typing import Optional, List

class ListNode:
    def __init__(self, val: int, next: Optional['ListNode']):
        self.val = val
        self.next = next


def list_node(values: List[int]) -> Optional[ListNode]:
    if not values:
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


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                while head.next is not None and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next