from collections import defaultdict
from math import inf

class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        groups = defaultdict(list)
        for index in range(len(nums)):
            groups[index % k].append(nums[index])

        freq = [defaultdict(int) for _ in range(k)]
        min_size = [inf] * k
        for index in range(k):
            for number in groups[index]:
                freq[index][number] += 1
            min_size[index] = len(groups[index])

        SIZE = 1 << 10  # 2^10
        dp = [inf] * SIZE
        dp[0] = 0

        for index in range(k):
            new_dp = [inf] * SIZE
            min_dp = min(dp)
            for state in range(SIZE):
                new_dp[state] = min_dp + min_size[index]
                for number, count in freq[index].items():
                    candidate_value = dp[state ^ number] + min_size[index] - count
                    if candidate_value < new_dp[state]:
                        new_dp[state] = candidate_value
            dp = new_dp

        return dp[0]