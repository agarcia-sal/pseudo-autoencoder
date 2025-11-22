class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(vals):
    if not vals:
        return None
    node = ListNode(vals[0])
    p = node
    for v in vals[1:]:
        p.next = ListNode(v)
        p = p.next
    return node

def is_same_list(p1, p2):
    if p1 is None and p2 is None:
        return True
    if p1 and p2 and p1.val == p2.val:
        return is_same_list(p1.next, p2.next)
    return False

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            f = cur.next
            s = cur.next.next
            cur.next = s
            f.next = s.next
            s.next = f
            cur = cur.next.next
        return dummy.next