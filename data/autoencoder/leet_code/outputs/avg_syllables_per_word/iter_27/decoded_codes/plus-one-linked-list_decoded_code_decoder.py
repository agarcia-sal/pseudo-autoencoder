from typing import Optional, List


class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def list_node(values_list: List[int]) -> Optional[ListNode]:
    if not values_list:
        return None
    head = ListNode(values_list[0])
    pointer = head
    for value in values_list[1:]:
        node = ListNode(value)
        pointer.next = node
        pointer = node
    return head


def is_same_list(pointer_one: Optional[ListNode], pointer_two: Optional[ListNode]) -> bool:
    if pointer_one is None and pointer_two is None:
        return True
    if pointer_one is None or pointer_two is None:
        return False
    return (
        pointer_one.val == pointer_two.val and
        is_same_list(pointer_one.next, pointer_two.next)
    )


class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(node: Optional[ListNode]) -> Optional[ListNode]:
            previous_node = None
            while node is not None:
                next_node = node.next
                node.next = previous_node
                previous_node = node
                node = next_node
            return previous_node

        reversed_head = reverseList(head)
        carry = 1
        current = reversed_head

        while current is not None and carry == 1:
            current.val += carry
            carry = current.val // 10
            current.val = current.val % 10

            if current.next is None and carry == 1:
                current.next = ListNode(carry)
                carry = 0

            previous_node = current
            current = current.next

        return reverseList(reversed_head)