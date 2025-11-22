from typing import List
import math

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        k = len(days[0]) if days else 0

        dp = [-1] * n
        dp[0] = 0

        graph = {i: [] for i in range(n)}
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
                candidate = dp[i] + days[i][week]
                if candidate > new_dp[i]:
                    new_dp[i] = candidate
                # Travel to connected cities
                for j in graph[i]:
                    candidate = dp[i] + days[j][week]
                    if candidate > new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        max_value = -math.inf
        for value in dp:
            if value > max_value:
                max_value = value

        return max_value