from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if n == 1:
            return False

        # dp[size] holds all possible sums of subsets of length size
        dp = [set() for _ in range(n // 2 + 1)]
        dp[0].add(0)

        for num in nums:
            # Iterate sizes in reverse to avoid reuse in the same iteration
            for size in range(n // 2, 0, -1):
                for s in dp[size - 1]:
                    new_sum = s + num
                    # Check the average condition
                    if new_sum * n == size * total_sum:
                        return True
                    dp[size].add(new_sum)
        return False