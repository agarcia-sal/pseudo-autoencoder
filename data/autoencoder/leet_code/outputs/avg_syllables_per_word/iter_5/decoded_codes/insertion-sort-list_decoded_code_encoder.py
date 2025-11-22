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
        p1, p2 = p1.next, p2.next
    return p1 is None and p2 is None

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(-5001)
        dummy.next = head
        current = head.next
        head.next = None
        while current:
            next_node = current.next
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = next_node
        return dummy.next