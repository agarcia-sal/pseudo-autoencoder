from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        total_citations = len(citations)
        left, right = 0, total_citations - 1
        h_index = 0

        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= total_citations - mid:
                h_index = total_citations - mid
                right = mid - 1
            else:
                left = mid + 1

        return h_index