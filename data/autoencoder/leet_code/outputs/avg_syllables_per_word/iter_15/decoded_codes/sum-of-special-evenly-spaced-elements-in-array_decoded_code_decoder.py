from typing import List

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(nums)
        if not queries:
            return []

        max_y = max(q[1] for q in queries)
        prefix_sums = [[0]*n for _ in range(max_y+1)]

        for y in range(1, max_y+1):
            for i in reversed(range(n)):
                if i + y < n:
                    prefix_sums[y][i] = nums[i] + prefix_sums[y][i + y]
                else:
                    prefix_sums[y][i] = nums[i]

        answer = []
        for x, y in queries:
            answer.append(prefix_sums[y][x] % MOD)

        return answer