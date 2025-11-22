class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for index in range(len(citations)):
            citation = citations[index]
            if citation < index + 1:
                return index
        return len(citations)