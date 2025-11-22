class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    p = head
    for v in vals[1:]:
        p.next = ListNode(v)
        p = p.next
    return head

def is_same_list(p1, p2):
    if p1 is None and p2 is None:
        return True
    if not p1 or not p2:
        return False
    return (p1.val == p2.val) and is_same_list(p1.next, p2.next)

class Solution:
    @staticmethod
    def insertionSortList(h):
        if not h or not h.next:
            return h
        dummy = ListNode(float('-inf'))
        dummy.next = h
        cur = h.next
        h.next = None
        while cur:
            nxt = cur.next
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt
        return dummy.next