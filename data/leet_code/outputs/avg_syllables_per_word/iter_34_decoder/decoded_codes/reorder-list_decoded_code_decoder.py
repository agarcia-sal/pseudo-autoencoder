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
        node = ListNode(val)
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
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        slow = head
        fast = head
        # Find middle (slow will be at middle)
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr is not None:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Merge two halves
        first = head
        second = prev
        while second.next is not None:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2