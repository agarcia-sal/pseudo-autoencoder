from collections import deque, defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q:
        n = q.popleft()
        if i < len(vals) and vals[i] is not None:
            n.left = TreeNode(vals[i])
            q.append(n.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            n.right = TreeNode(vals[i])
            q.append(n.right)
        i += 1
    return root

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)

        def subtree_sum(n: Optional[TreeNode]) -> int:
            if not n:
                return 0
            s = n.val + subtree_sum(n.left) + subtree_sum(n.right)
            count[s] += 1
            return s

        subtree_sum(root)
        max_freq = max(count.values(), default=0)
        return [k for k, v in count.items() if v == max_freq]