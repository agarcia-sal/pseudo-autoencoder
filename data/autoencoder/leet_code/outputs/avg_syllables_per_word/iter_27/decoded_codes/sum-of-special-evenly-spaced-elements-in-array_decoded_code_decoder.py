from typing import List

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(nums)
        if not queries:
            return []

        max_y = max(query[1] for query in queries if len(query) > 1)
        prefix_sums = [[0] * n for _ in range(max_y + 1)]

        for y in range(1, max_y + 1):
            for i in range(n - 1, -1, -1):
                if i + y < n:
                    prefix_sums[y][i] = nums[i] + prefix_sums[y][i + y]
                else:
                    prefix_sums[y][i] = nums[i]

        answer = []
        for query in queries:
            if len(query) != 2:
                # Handle invalid query gracefully by appending 0 or ignoring
                answer.append(0)
                continue
            x, y = query
            if 0 <= y <= max_y and 0 <= x < n:
                answer.append(prefix_sums[y][x] % MOD)
            else:
                # If query indices are out of bounds, append 0 gracefully
                answer.append(0)

        return answer