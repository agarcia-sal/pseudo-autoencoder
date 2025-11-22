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
    if not p1 and not p2:
        return True
    if not p1 or not p2:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)

class Solution:
    @staticmethod
    def reverseBetween(head, left, right):
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next

        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next