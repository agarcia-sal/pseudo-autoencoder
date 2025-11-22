class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        total_sum = sum(nums)
        half = n // 2
        dp = [set() for _ in range(half + 1)]
        dp[0].add(0)

        for num in nums:
            for size in range(half, 0, -1):
                for s in dp[size - 1]:
                    new_sum = s + num
                    if new_sum * n == size * total_sum:
                        return True
                    dp[size].add(new_sum)
        return False