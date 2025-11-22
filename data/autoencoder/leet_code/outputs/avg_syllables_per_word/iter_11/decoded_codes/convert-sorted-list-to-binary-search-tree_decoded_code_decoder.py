from collections import deque

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def list_node(values):
    if not values:
        return None
    head = ListNode(values[0], None)
    p = head
    for val in values[1:]:
        node = ListNode(val, None)
        p.next = node
        p = node
    return head

def is_same_list(p1, p2):
    if p1 is None and p2 is None:
        return True
    if p1 is None or p2 is None:
        return False
    return (p1.val == p2.val) and is_same_list(p1.next, p2.next)

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None
    root = TreeNode(values[0], None, None)
    i = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i], None, None)
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i], None, None)
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def sortedListToBST(self, head):
        if head is None:
            return None

        def findMiddle(left, right):
            slow = left
            fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def convertListToBST(left, right):
            if left == right:
                return None
            mid = findMiddle(left, right)
            node = TreeNode(mid.val, None, None)
            node.left = convertListToBST(left, mid)
            node.right = convertListToBST(mid.next, right)
            return node

        return convertListToBST(head, None)