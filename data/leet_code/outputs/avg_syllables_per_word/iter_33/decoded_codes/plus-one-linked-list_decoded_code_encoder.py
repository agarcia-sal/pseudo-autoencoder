class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_node(values):
    if len(values) == 0:
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
    def plusOne(self, head):
        def reverseList(node):
            prev = None
            while node is not None:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        reversed_head = reverseList(head)
        carry = 1
        current = reversed_head

        while current is not None and carry == 1:
            current.val += carry
            carry = current.val // 10
            current.val %= 10

            if current.next is None and carry == 1:
                current.next = ListNode(carry)
                carry = 0

            current = current.next

        return reverseList(reversed_head)