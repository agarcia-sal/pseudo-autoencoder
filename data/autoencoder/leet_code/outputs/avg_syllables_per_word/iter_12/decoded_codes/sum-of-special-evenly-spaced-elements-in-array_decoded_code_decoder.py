class Solution:
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)

        max_y = max(y for _, y in queries) if queries else 0

        def initialize_prefix_sums(max_y, n):
            return [[0] * n for _ in range(max_y + 1)]

        prefix_sums = initialize_prefix_sums(max_y, n)

        for y in range(1, max_y + 1):
            for i in range(n - 1, -1, -1):
                if i + y < n:
                    prefix_sums[y][i] = nums[i] + prefix_sums[y][i + y]
                else:
                    prefix_sums[y][i] = nums[i]

        answer = []
        for x, y in queries:
            result = prefix_sums[y][x]
            answer.append(result % MOD)

        return answer