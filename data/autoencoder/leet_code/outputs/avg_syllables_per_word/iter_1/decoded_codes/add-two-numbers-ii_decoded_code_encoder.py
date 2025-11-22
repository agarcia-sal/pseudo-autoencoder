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
    if p1 is None and p2 is None:
        return True
    if not p1 or not p2:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)

class Solution:
    def addTwoNumbers(self, l1, l2):
        def pushIntoStack(n):
            s = []
            while n:
                s.append(n.val)
                n = n.next
            return s

        s1 = pushIntoStack(l1)
        s2 = pushIntoStack(l2)
        carry = 0
        res = None

        while s1 or s2 or carry:
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            d = total % 10
            node = ListNode(d)
            node.next = res
            res = node

        return res