from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def pushIntoStack(node: Optional[ListNode]) -> List[int]:
            stack = []
            while node is not None:
                stack.append(node.val)
                node = node.next
            return stack

        stack1 = pushIntoStack(l1)
        stack2 = pushIntoStack(l2)

        carry = 0
        result = None

        while stack1 or stack2 or carry != 0:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            new_node = ListNode(digit)
            new_node.next = result
            result = new_node

        return result