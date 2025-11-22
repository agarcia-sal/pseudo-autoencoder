import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def list_node(values: List[int]) -> Optional[ListNode]:
    if len(values) == 0:
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        i = 0
        for lst in lists:
            if lst is not None:
                heapq.heappush(min_heap, (lst.val, i, lst))
            i += 1

        dummy = ListNode()
        current = dummy
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next