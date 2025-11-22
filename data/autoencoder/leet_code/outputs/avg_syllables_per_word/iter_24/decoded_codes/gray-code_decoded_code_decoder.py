from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prev_gray = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        reversed_prev_gray = prev_gray[::-1]
        current_gray = prev_gray[:]
        for number in reversed_prev_gray:
            current_gray.append(mask | number)
        return current_gray