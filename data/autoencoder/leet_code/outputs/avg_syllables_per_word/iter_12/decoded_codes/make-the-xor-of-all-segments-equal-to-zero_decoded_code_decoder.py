from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums, k):
        groups = defaultdict(list)
        for index in range(len(nums)):
            groups[index % k].append(nums[index])

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k

        for index in range(k):
            for num in groups[index]:
                freq[index][num] += 1
            min_size[index] = len(groups[index])

        dp = [inf] * (1 << 10)
        dp[0] = 0

        for index in range(k):
            new_dp = [inf] * (1 << 10)
            min_dp = min(dp)
            for j in range(1 << 10):
                new_dp[j] = min_dp + min_size[index]
                for number, count in freq[index].items():
                    candidate_value = dp[j ^ number] + min_size[index] - count
                    if candidate_value < new_dp[j]:
                        new_dp[j] = candidate_value
            dp = new_dp

        return dp[0]