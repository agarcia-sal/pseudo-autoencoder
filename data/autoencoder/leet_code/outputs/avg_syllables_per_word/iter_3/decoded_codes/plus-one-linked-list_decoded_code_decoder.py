class ListNode:
    def __init__(self, val=0, next=None):
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
    if p1 is None and p2 is None:
        return True
    if p1 is None or p2 is None:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)

class Solution:
    def plusOne(self, head):
        def reverseList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        reversed_head = reverseList(head)
        carry = 1
        current = reversed_head

        while current and carry:
            current.val += carry
            carry = current.val // 10
            current.val %= 10
            if current.next is None and carry:
                current.next = ListNode(carry)
                carry = 0
            current = current.next

        return reverseList(reversed_head)