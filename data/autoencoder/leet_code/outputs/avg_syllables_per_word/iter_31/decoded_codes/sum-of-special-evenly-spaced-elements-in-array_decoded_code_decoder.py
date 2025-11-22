from typing import List

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(nums)
        if not queries:
            return []

        max_y = max((q[1] for q in queries), default=0)
        if max_y == 0:
            # If max_y is zero, all queries have y=0, sum is just nums[x]
            # Ensure queries have valid x indices; return nums[x] % MOD for each query
            return [nums[q[0]] % MOD for q in queries]

        # prefix_sums[y][i] = nums[i] + prefix_sums[y][i + y] if i + y < n else nums[i]
        # Precompute prefix sums for each y from 1 to max_y
        prefix_sums = [[0] * n for _ in range(max_y + 1)]

        for y in range(1, max_y + 1):
            for i in range(n - 1, -1, -1):
                if i + y < n:
                    prefix_sums[y][i] = (nums[i] + prefix_sums[y][i + y]) % MOD
                else:
                    prefix_sums[y][i] = nums[i] % MOD

        answer = []
        for x, y in queries:
            if 0 <= y <= max_y and 0 <= x < n:
                answer.append(prefix_sums[y][x] % MOD)
            else:
                # Queries with invalid indices return 0 as a safe fallback
                answer.append(0)

        return answer