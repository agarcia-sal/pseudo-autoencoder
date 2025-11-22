from collections import defaultdict

class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        groups = defaultdict(list)
        n = len(nums)
        for i in range(n):
            groups[i % k].append(nums[i])

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [float('inf')] * k

        for i in range(k):
            current_group = groups[i]
            for num in current_group:
                freq[i][num] += 1
            min_size[i] = len(current_group)

        limit = 1 << 10  # 2^10
        dp = [float('inf')] * limit
        dp[0] = 0

        for i in range(k):
            new_dp = [float('inf')] * limit
            min_dp = min(dp)
            for j in range(limit):
                # worst case: change all elements of current group
                new_dp[j] = min_dp + min_size[i]
                for num, count in freq[i].items():
                    candidate = dp[j ^ num] + min_size[i] - count
                    if candidate < new_dp[j]:
                        new_dp[j] = candidate
            dp = new_dp

        return dp[0]