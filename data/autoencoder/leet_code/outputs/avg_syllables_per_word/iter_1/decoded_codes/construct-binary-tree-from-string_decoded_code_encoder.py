class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    def parse(i):
        if i >= len(s):
            return None, i
        start = i
        while i < len(s) and (s[i].isdigit() or s[i] == '-'):
            i += 1
        n = TreeNode(int(s[start:i]))
        if i < len(s) and s[i] == '(':
            n.left, i = parse(i + 1)
        if i < len(s) and s[i] == '(':
            n.right, i = parse(i + 1)
        if i < len(s) and s[i] == ')':
            i += 1
        return n, i
    root, _ = parse(0)
    return root