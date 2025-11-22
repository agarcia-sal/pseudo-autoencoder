class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i in range(len(citations)):
            citation = citations[i]
            if citation < i + 1:
                return i
        return len(citations)