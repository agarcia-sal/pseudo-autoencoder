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
                cost_option = left_costs[i - 1] + 2
                if i + 1 <= cost_option:
                    left_costs[i] = i + 1
                else:
                    left_costs[i] = cost_option

        right_costs[-1] = 1 if s[-1] == '1' else 0

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                right_costs[i] = right_costs[i + 1]
            else:
                cost_option = right_costs[i + 1] + 2
                dist_to_end = n - i
                if dist_to_end <= cost_option:
                    right_costs[i] = dist_to_end
                else:
                    right_costs[i] = cost_option

        min_time = left_costs[-1] if left_costs[-1] <= right_costs[0] else right_costs[0]

        for i in range(n - 1):
            combined_cost = left_costs[i] + right_costs[i + 1]
            if combined_cost < min_time:
                min_time = combined_cost

        return min_time