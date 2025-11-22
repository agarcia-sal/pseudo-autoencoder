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
    return (p1 is None and p2 is None) or (p1 and p2 and p1.val == p2.val and is_same_list(p1.next, p2.next))

class Solution:
    @staticmethod
    def sortList(head):
        if not head or not head.next:
            return head

        def split(h):
            slow, fast = h, h.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid, slow.next = slow.next, None
            return h, mid

        def merge(l1, l2):
            dummy = cur = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next, l1 = l1, l1.next
                else:
                    cur.next, l2 = l2, l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next

        left, right = split(head)
        left = Solution.sortList(left)
        right = Solution.sortList(right)
        return merge(left, right)