class Solution:
    def minChanges(self, nums, k):
        from collections import defaultdict

        groups = [[] for _ in range(k)]
        for i, num in enumerate(nums):
            groups[i % k].append(num)

        freq = []
        min_size = []
        for group in groups:
            counter = defaultdict(int)
            for num in group:
                counter[num] += 1
            freq.append(counter)
            min_size.append(len(group))

        MAX_XOR = 1 << 10
        INF = float('inf')
        dp = [INF] * MAX_XOR
        dp[0] = 0

        for i in range(k):
            new_dp = [INF] * MAX_XOR
            min_dp = min(dp)
            for j in range(MAX_XOR):
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    candidate = dp[j ^ num] + min_size[i] - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        return dp[0]