from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result: List[int] = []
        # Append from 1 to n-k-1
        for number in range(1, n - k):
            result.append(number)
        left, right = n - k, n
        while left <= right:
            if left == right:
                result.append(left)
            else:
                result.append(left)
                result.append(right)
            left += 1
            right -= 1
        return result