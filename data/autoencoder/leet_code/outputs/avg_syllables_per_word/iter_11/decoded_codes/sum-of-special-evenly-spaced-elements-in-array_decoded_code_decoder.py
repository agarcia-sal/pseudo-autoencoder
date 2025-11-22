class Solution:
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)

        max_y = max(y for _, y in queries) if queries else 0
        prefix_sums = self.init_prefix_sums(max_y + 1, n)

        for y in range(1, max_y + 1):
            for i in range(n - 1, -1, -1):
                if i + y < n:
                    prefix_sums[y][i] = nums[i] + prefix_sums[y][i + y]
                else:
                    prefix_sums[y][i] = nums[i]

        answer = []
        for x, y in queries:
            answer.append(prefix_sums[y][x] % MOD)
        return answer

    def init_prefix_sums(self, rows, cols):
        prefix_sums = []
        for _ in range(rows):
            prefix_sums.append([0] * cols)
        return prefix_sums