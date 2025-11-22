from typing import List

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(nums)
        if not queries:
            return []

        max_y = max(y for _, y in queries)

        # prefix_sums[y][i] will store the sum starting at index i with step y
        prefix_sums = [[0] * n for _ in range(max_y + 1)]

        for y in range(1, max_y + 1):
            for i in range(n - 1, -1, -1):
                if i + y < n:
                    prefix_sums[y][i] = nums[i] + prefix_sums[y][i + y]
                else:
                    prefix_sums[y][i] = nums[i]

        answer = []
        for x, y in queries:
            # Safely handle edge cases where x or y might be out of bounds
            if 0 <= y <= max_y and 0 <= x < n:
                answer.append(prefix_sums[y][x] % MOD)
            else:
                # If out of bounds, sum is assumed zero (not specified in pseudocode,
                # but this is a safe fallback)
                answer.append(0)

        return answer