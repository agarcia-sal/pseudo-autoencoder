import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(values):
    if len(values) == 0:
        return None
    head = ListNode(values[0])
    p = head
    for val in values[1:]:
        node = ListNode(val)
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
    def mergeKLists(self, lists):
        min_heap = []
        i = 1
        for lst in lists:
            if lst is not None:
                heapq.heappush(min_heap, (lst.val, i, lst))
            i += 1

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next