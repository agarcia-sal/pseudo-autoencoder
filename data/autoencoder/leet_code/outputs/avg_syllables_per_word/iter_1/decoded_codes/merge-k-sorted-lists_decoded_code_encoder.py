import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    dummy = cur = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next