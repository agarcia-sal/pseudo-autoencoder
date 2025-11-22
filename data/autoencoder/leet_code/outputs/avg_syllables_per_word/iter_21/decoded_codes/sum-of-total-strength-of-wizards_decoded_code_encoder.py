class Solution:
    def totalStrength(self, strength):
        MOD = 10**9 + 7
        n = len(strength)

        prefix = self.initialize_prefix_sums(strength, n, MOD)
        prefix_prefix = self.initialize_prefix_prefix_sums(prefix, n, MOD)
        prev_smaller = self.initialize_prev_smaller(strength, n)
        next_smaller_or_equal = self.initialize_next_smaller_or_equal(strength, n)

        total_strength = 0
        for index in range(n):
            left = prev_smaller[index] + 1
            right = next_smaller_or_equal[index]

            sum_left = (index - left + 1) * (prefix_prefix[right + 1] - prefix_prefix[index + 1]) % MOD
            sum_right = (right - index) * (prefix_prefix[index + 1] - prefix_prefix[left]) % MOD

            contribution = strength[index] * (sum_left - sum_right) % MOD
            total_strength = (total_strength + contribution) % MOD

        return total_strength

    def initialize_prefix_sums(self, strength, n, MOD):
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD
        return prefix

    def initialize_prefix_prefix_sums(self, prefix, n, MOD):
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MOD
        return prefix_prefix

    def initialize_prev_smaller(self, strength, n):
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        return prev_smaller

    def initialize_next_smaller_or_equal(self, strength, n):
        next_smaller_or_equal = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                next_smaller_or_equal[i] = stack[-1]
            stack.append(i)
        return next_smaller_or_equal