from heapq import heappush, heappop
from typing import List, Optional

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, lst in enumerate(lists):
            if lst:
                heappush(min_heap, (lst.val, i, lst))
        dummy = ListNode(0)
        current = dummy
        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next