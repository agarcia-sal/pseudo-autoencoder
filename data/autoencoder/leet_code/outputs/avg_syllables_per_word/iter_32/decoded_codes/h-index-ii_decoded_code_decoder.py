from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        h_index = 0
        while left <= right:
            mid = left + (right - left) // 2
            # Number of papers with at least citations[mid] citations is n - mid
            if citations[mid] >= n - mid:
                h_index = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return h_index