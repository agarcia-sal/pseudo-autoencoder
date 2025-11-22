class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    f = s = dummy
    for _ in range(n+1):
        f = f.next
    while f:
        f = f.next
        s = s.next
    s.next = s.next.next
    return dummy.next