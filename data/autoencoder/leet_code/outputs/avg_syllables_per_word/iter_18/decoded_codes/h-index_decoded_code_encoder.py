from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        self.sort_citations_descending(citations)
        for index, citation in enumerate(citations):
            if citation < index + 1:
                return index
        return len(citations)

    def sort_citations_descending(self, citations: List[int]) -> None:
        citations.sort(reverse=True)