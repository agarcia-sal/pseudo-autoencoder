from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional['ListNode']):
        self.val = val
        self.next = next


def list_node(values):
    if len(values) == 0:
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next