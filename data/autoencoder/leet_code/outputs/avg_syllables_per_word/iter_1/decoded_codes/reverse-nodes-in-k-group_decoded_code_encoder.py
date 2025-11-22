class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(start, end):
    prev, curr = None, start
    while curr != end:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    curr.next = prev
    return end, start

def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev_end = dummy

    while True:
        kth = prev_end
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next
        next_start = kth.next
        kth.next = None
        new_start, new_end = reverseLinkedList(prev_end.next, kth)
        prev_end.next = new_start
        new_end.next = next_start
        prev_end = new_end