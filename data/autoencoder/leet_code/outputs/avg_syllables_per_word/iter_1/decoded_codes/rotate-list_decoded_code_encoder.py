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
        n = ListNode(v)
        p.next = n
        p = n
    return head

def is_same_list(p1, p2):
    if not p1 and not p2:
        return True
    if not p1 or not p2:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head
        k %= length
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head