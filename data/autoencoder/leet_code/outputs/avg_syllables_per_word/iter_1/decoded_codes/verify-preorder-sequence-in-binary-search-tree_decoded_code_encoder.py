def verifyPreorder(preorder):
    stack = []
    lower = float('-inf')
    for v in preorder:
        if v < lower:
            return False
        while stack and v > stack[-1]:
            lower = stack.pop()
        stack.append(v)
    return True