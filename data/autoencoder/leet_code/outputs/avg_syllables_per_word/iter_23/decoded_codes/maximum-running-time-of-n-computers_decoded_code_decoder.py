from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def canRunFor(time: int) -> bool:
            total = 0
            for battery in batteries:
                total += min(battery, time)
            return total >= time * n

        left, right = 0, sum(batteries) // n

        while left < right:
            mid = (left + right + 1) // 2
            if canRunFor(mid):
                left = mid
            else:
                right -= 1

        return left