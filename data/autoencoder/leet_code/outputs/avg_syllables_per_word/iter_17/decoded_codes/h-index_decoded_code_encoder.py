class Solution:
    def hIndex(self, list_of_citations):
        list_of_citations.sort(reverse=True)
        for index in range(len(list_of_citations)):
            citation_to_check = list_of_citations[index]
            if citation_to_check < index + 1:
                return index
        return len(list_of_citations)