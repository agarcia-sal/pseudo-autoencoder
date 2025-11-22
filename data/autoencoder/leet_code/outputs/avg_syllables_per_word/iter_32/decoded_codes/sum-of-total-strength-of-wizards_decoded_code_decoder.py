from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MODULO = 10**9 + 7
        n = len(strength)

        # prefix[i] = sum of strength[0..i-1] mod MODULO
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MODULO

        # prefix_prefix[i] = sum of prefix[0..i-1] mod MODULO
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MODULO

        prev_smaller = [-1] * n
        next_smaller_or_equal = [n] * n

        stack = []
        # Find previous smaller elements (strictly smaller)
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        stack.clear()
        # Find next smaller or equal elements
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                next_smaller_or_equal[i] = stack[-1]
            stack.append(i)

        total_strength = 0
        for i in range(n):
            left_boundary = prev_smaller[i] + 1
            right_boundary = next_smaller_or_equal[i]

            # sum_left:
            # number of subarrays starting between left_boundary and i (inclusive) * sum of prefix at right_boundary+1 - prefix at i+1
            sum_left = (i - left_boundary + 1) * (prefix_prefix[right_boundary + 1] - prefix_prefix[i + 1]) % MODULO

            # sum_right:
            # number of subarrays starting between i and right_boundary-1 (inclusive) * sum of prefix at i+1 - prefix at left_boundary
            sum_right = (right_boundary - i) * (prefix_prefix[i + 1] - prefix_prefix[left_boundary]) % MODULO

            contribution = strength[i] * (sum_left - sum_right) % MODULO
            total_strength = (total_strength + contribution) % MODULO

        return total_strength