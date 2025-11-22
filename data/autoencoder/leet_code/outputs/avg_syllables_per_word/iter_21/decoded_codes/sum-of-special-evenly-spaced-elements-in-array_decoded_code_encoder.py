class Solution:
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        max_y = max(y for _, y in queries) if queries else 0

        # Initialize prefix_sums: a list of lists with zeroes, for y in [0..max_y], each list length n
        prefix_sums = [[0] * n for _ in range(max_y + 1)]

        # For y=0, prefix_sums[y] is just nums itself
        if n > 0:
            prefix_sums[0] = nums[:]

        # Compute prefix sums for y from 1 to max_y
        for y in range(1, max_y + 1):
            for i in range(n - 1, -1, -1):
                if i + y < n:
                    prefix_sums[y][i] = (nums[i] + prefix_sums[y][i + y]) % MOD
                else:
                    prefix_sums[y][i] = nums[i] % MOD

        answer = []
        for x, y in queries:
            answer.append(prefix_sums[y][x] % MOD)

        return answer