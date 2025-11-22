class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def list_node(values):
    if not values:
        return None
    head = ListNode(values[0])
    p = head
    for val in values[1:]:
        p.next = ListNode(val)
        p = p.next
    return head

def is_same_list(p1, p2):
    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return p1 is None and p2 is None

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head