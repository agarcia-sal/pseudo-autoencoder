class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for index, citation in enumerate(citations):
            if citation < index + 1:
                return index
        return len(citations)