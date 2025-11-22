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
                # Staying in the same city
                if dp[i] + days[i][week] > new_dp[i]:
                    new_dp[i] = dp[i] + days[i][week]
                # Traveling to other cities reachable from city i
                for j in graph[i]:
                    val = dp[i] + days[j][week]
                    if val > new_dp[j]:
                        new_dp[j] = val
            dp = new_dp

        return max(dp)