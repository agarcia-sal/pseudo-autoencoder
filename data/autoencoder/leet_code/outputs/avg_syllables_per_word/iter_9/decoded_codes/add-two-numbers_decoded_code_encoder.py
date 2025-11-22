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
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next