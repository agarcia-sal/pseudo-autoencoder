class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(values):
    if not values:
        return None
    head = ListNode(val=values[0])
    p = head
    for val in values[1:]:
        node = ListNode(val=val)
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
    def partition(self, head, x):
        less_head = ListNode(val=0)
        greater_head = ListNode(val=0)
        less = less_head
        greater = greater_head
        current = head
        while current is not None:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        less.next = greater_head.next
        greater.next = None
        return less_head.next