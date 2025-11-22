def find132pattern(nums):
    second = float('-inf')
    stack = []

    for num in reversed(nums):
        if num < second:
            return True
        while stack and stack[-1] < num:
            second = stack.pop()
        stack.append(num)

    return False