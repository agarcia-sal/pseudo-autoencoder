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
    def addTwoNumbers(self, l1, l2):
        def pushIntoStack(node):
            stack = []
            while node is not None:
                stack.append(node.val)
                node = node.next
            return stack

        stack1 = pushIntoStack(l1)
        stack2 = pushIntoStack(l2)

        carry = 0
        result = None

        while len(stack1) > 0 or len(stack2) > 0 or carry != 0:
            if len(stack1) > 0:
                val1 = stack1.pop()
            else:
                val1 = 0
            if len(stack2) > 0:
                val2 = stack2.pop()
            else:
                val2 = 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            new_node = ListNode(digit)
            new_node.next = result
            result = new_node

        return result