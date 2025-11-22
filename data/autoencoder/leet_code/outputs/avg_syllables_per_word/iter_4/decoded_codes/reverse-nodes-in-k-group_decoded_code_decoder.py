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
    return (p1.val == p2.val) and is_same_list(p1.next, p2.next)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(start: ListNode, end: ListNode) -> (ListNode, ListNode):
            prev = None
            curr = start
            while curr is not end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            curr.next = prev
            return end, start

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            kth_node = prev_group_end
            for _ in range(k):
                kth_node = kth_node.next
                if kth_node is None:
                    return dummy.next

            next_group_start = kth_node.next
            kth_node.next = None
            new_group_start, new_group_end = reverseLinkedList(prev_group_end.next, kth_node)

            prev_group_end.next = new_group_start
            new_group_end.next = next_group_start

            prev_group_end = new_group_end