class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        left_costs = [0] * n
        right_costs = [0] * n

        # Calculate left costs
        left_costs[0] = 1 if s[0] == '1' else 0
        for i in range(1, n):
            if s[i] == '0':
                left_costs[i] = left_costs[i - 1]
            else:
                candidate_one = i + 1
                candidate_two = left_costs[i - 1] + 2
                left_costs[i] = candidate_one if candidate_one < candidate_two else candidate_two

        # Calculate right costs
        right_costs[n - 1] = 1 if s[n - 1] == '1' else 0
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                right_costs[i] = right_costs[i + 1]
            else:
                candidate_one = n - i
                candidate_two = right_costs[i + 1] + 2
                right_costs[i] = candidate_one if candidate_one < candidate_two else candidate_two

        # Calculate minimum time by combining left and right costs
        min_time = left_costs[n - 1] if left_costs[n - 1] < right_costs[0] else right_costs[0]
        for i in range(n - 1):
            candidate_time = left_costs[i] + right_costs[i + 1]
            if candidate_time < min_time:
                min_time = candidate_time

        return min_time