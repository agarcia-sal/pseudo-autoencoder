from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        k = len(days[0])

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
                current_score = dp[i] + days[i][week]
                if current_score > new_dp[i]:
                    new_dp[i] = current_score
                for j in graph[i]:
                    possible_score = dp[i] + days[j][week]
                    if possible_score > new_dp[j]:
                        new_dp[j] = possible_score
            dp = new_dp

        return max(dp) if dp else -1