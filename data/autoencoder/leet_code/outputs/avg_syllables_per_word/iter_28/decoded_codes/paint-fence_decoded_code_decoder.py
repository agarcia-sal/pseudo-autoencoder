from typing import Optional

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        same = k
        diff = k * (k - 1)
        total = same + diff
        for _ in range(3, n + 1):
            new_same = diff
            new_diff = total * (k - 1)
            same, diff = new_same, new_diff
            total = same + diff
        return total