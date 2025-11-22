from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prev_gray = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        # Append reversed prev_gray with mask ORed to each element
        current_gray = prev_gray + [mask | num for num in reversed(prev_gray)]
        return current_gray