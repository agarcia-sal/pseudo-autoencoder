import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        left, right = 1, max(piles) if piles else 1

        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left