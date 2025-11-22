class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        left_costs = [0] * n
        right_costs = [0] * n

        left_costs[0] = 1 if s[0] == '1' else 0
        for i in range(1, n):
            if s[i] == '0':
                left_costs[i] = left_costs[i - 1]
            else:
                left_costs[i] = min(i + 1, left_costs[i - 1] + 2)

        right_costs[-1] = 1 if s[-1] == '1' else 0
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                right_costs[i] = right_costs[i + 1]
            else:
                right_costs[i] = min(n - i, right_costs[i + 1] + 2)

        min_time = min(left_costs[-1], right_costs[0])

        for i in range(n - 1):
            min_time = min(min_time, left_costs[i] + right_costs[i + 1])

        return min_time