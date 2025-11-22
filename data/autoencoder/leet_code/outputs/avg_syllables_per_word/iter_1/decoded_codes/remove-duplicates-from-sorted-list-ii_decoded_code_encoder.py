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
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next