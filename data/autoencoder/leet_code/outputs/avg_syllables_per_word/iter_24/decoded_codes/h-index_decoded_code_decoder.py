from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for index in range(len(citations)):
            if citations[index] < index + 1:
                return index
        return len(citations)