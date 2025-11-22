from typing import List, Dict

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        if n == 0:
            return 0
        k = len(days[0]) if days else 0
        if k == 0:
            return 0

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
                stay = dp[i] + days[i][week]
                if new_dp[i] < stay:
                    new_dp[i] = stay
                # Travel to connected cities
                for j in graph[i]:
                    travel = dp[i] + days[j][week]
                    if new_dp[j] < travel:
                        new_dp[j] = travel
            dp = new_dp

        max_value = max(dp) if dp else -float('inf')
        return max_value