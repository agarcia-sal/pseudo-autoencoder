from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)

        if n == 1:
            return False

        dp = self.initializeSetList(n // 2 + 1)
        self.addZeroToSet(dp[0])

        for num in nums:
            for size in range(n // 2, 0, -1):
                for s in dp[size - 1]:
                    new_sum = s + num
                    if new_sum * n == size * total_sum:
                        return True
                    self.addSumToSet(dp[size], new_sum)

        return False

    def initializeSetList(self, length: int) -> List[set]:
        # Creates a list of empty sets of given length
        return [set() for _ in range(length)]

    def addZeroToSet(self, s: set) -> None:
        # Adds zero sum to the set to indicate empty subset sum
        s.add(0)

    def addSumToSet(self, s: set, val: int) -> None:
        # Adds a new sum val to the given set
        s.add(val)