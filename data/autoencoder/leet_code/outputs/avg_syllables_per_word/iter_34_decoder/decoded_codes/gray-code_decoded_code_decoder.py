from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prev_gray = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        current_gray = prev_gray + [x | mask for x in reversed(prev_gray)]
        return current_gray