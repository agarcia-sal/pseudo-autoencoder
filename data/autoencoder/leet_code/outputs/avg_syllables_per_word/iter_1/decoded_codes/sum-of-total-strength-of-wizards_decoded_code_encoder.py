def total_strength(strength):
    MOD = 10**9 + 7
    n = len(strength)

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = (prefix[i] + strength[i]) % MOD

    prefix_prefix = [0] * (n + 2)
    for i in range(n + 1):
        prefix_prefix[i+1] = (prefix_prefix[i] + prefix[i]) % MOD

    prev_smaller = [-1] * n
    next_smaller_eq = [n] * n

    stack = []
    for i in range(n):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()
    for i in range(n-1, -1, -1):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        next_smaller_eq[i] = stack[-1] if stack else n
        stack.append(i)

    total = 0
    for i in range(n):
        L = prev_smaller[i] + 1
        R = next_smaller_eq[i]
        left_sum = (i - L + 1) * (prefix_prefix[R + 1] - prefix_prefix[i + 1]) % MOD
        right_sum = (R - i) * (prefix_prefix[i + 1] - prefix_prefix[L]) % MOD
        contribution = strength[i] * (left_sum - right_sum) % MOD
        total = (total + contribution) % MOD

    return total