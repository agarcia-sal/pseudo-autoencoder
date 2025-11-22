from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val = val
        self.next = next

def list_node(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    p = head
    for val in values[1:]:
        node = ListNode(val)
        p.next = node
        p = node
    return head

def is_same_list(p1: Optional[ListNode], p2: Optional[ListNode]) -> bool:
    if p1 is None and p2 is None:
        return True
    if p1 is None or p2 is None:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def split(head: ListNode) -> (ListNode, ListNode):
            slow = head
            fast = head.next
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 is not None else l2
            return dummy.next

        left, right = split(head)
        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left, right)