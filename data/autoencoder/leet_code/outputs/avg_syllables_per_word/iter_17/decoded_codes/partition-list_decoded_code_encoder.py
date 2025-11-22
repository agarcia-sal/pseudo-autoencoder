class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(values_list):
    if not values_list:
        return None
    head = ListNode(values_list[0])
    pointer = head
    for value in values_list[1:]:
        node = ListNode(value)
        pointer.next = node
        pointer = node
    return head

def is_same_list(pointer_one, pointer_two):
    if pointer_one is None and pointer_two is None:
        return True
    if pointer_one is None or pointer_two is None:
        return False
    return pointer_one.val == pointer_two.val and is_same_list(pointer_one.next, pointer_two.next)

class Solution:
    def partition(self, head_node, x_value):
        less_head = ListNode(0)
        greater_head = ListNode(0)

        less = less_head
        greater = greater_head

        current = head_node
        while current is not None:
            if current.val < x_value:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        less.next = greater_head.next
        greater.next = None

        return less_head.next