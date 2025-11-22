from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city: int) -> None:
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                province_count += 1

        return province_count