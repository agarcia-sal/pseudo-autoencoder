from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for index, citation in enumerate(citations):
            if citation < index + 1:
                return index
        return len(citations)