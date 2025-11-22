from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
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
    return pointer_one.val == pointer_two.val and is_same_list(pointer_one.next, pointer_two.next)


class Solution:
    def sortList(self, head_pointer: Optional[ListNode]) -> Optional[ListNode]:
        if head_pointer is None or head_pointer.next is None:
            return head_pointer

        def split(head_parameter: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
            slow = head_parameter
            fast = head_parameter.next
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head_parameter, mid

        def merge(list_one: Optional[ListNode], list_two: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy
            while list_one is not None and list_two is not None:
                if list_one.val < list_two.val:
                    current.next = list_one
                    list_one = list_one.next
                else:
                    current.next = list_two
                    list_two = list_two.next
                current = current.next
            current.next = list_one or list_two
            return dummy.next

        left_part, right_part = split(head_pointer)
        left_part = self.sortList(left_part)
        right_part = self.sortList(right_part)

        return merge(left_part, right_part)