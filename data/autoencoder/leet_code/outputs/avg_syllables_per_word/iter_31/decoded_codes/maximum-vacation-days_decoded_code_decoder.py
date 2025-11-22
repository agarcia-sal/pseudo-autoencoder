from typing import List, Dict

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        k = len(days[0]) if days else 0

        dp = [-1] * n
        dp[0] = 0

        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if flights[i][j] == 1:
                    graph[i].append(j)

        for week in range(k):
            new_dp = [-1] * n
            for i in range(n):
                if dp[i] == -1:
                    continue
                # Stay in the same city
                new_val_same_city = dp[i] + days[i][week]
                if new_val_same_city > new_dp[i]:
                    new_dp[i] = new_val_same_city
                # Travel to connected cities
                for j in graph[i]:
                    new_val_travel = dp[i] + days[j][week]
                    if new_val_travel > new_dp[j]:
                        new_dp[j] = new_val_travel
            dp = new_dp

        max_value = max(dp) if dp else -1
        return max_value