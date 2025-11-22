class Solution:
    def hIndex(self, citations_list):
        number_of_citations = len(citations_list)
        left_pointer = 0
        right_pointer = number_of_citations - 1
        h_index_value = 0

        while left_pointer <= right_pointer:
            middle_position = left_pointer + (right_pointer - left_pointer) // 2
            if citations_list[middle_position] >= number_of_citations - middle_position:
                h_index_value = number_of_citations - middle_position
                right_pointer = middle_position - 1
            else:
                left_pointer = middle_position + 1

        return h_index_value