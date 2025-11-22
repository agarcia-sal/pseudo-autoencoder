from typing import Callable

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x: int) -> bool:
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count >= k

        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        return low