from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 1
        n = len(strength)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD

        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MOD

        prev_smaller = [-1] * n
        next_smaller_or_equal = [n] * n

        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                next_smaller_or_equal[i] = stack[-1]
            stack.append(i)

        total_strength = 0
        for i in range(n):
            left = prev_smaller[i] + 1
            right = next_smaller_or_equal[i]

            sum_left = (i - left + 1) * ((prefix_prefix[right + 1] - prefix_prefix[i + 1]) % MOD) % MOD
            sum_right = (right - i) * ((prefix_prefix[i + 1] - prefix_prefix[left]) % MOD) % MOD

            contribution = strength[i] * ((sum_left - sum_right) % MOD) % MOD
            total_strength = (total_strength + contribution) % MOD

        return total_strength