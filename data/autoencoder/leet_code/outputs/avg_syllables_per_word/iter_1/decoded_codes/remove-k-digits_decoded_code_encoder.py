def removeKdigits(num: str, k: int) -> str:
    stack = []
    for d in num:
        while k > 0 and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)
    final_stack = stack[:-k] if k > 0 else stack
    result = ''.join(final_stack).lstrip('0')
    return result if result != '' else "0"