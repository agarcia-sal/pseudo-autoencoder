from typing import List

def GenerateListWithMultipleElementsOfValue(length_value: int, element_value: int) -> List[int]:
    # Returns a list of length `length_value` filled with `element_value`.
    return [element_value] * length_value

def AllCharactersNonDecreasing(list_of_strings: List[str], number_of_rows: int, index_j: int, index_i: int) -> bool:
    # Returns True if for every string in list_of_strings,
    # character at index_j <= character at index_i.
    for k in range(number_of_rows):
        if list_of_strings[k][index_j] > list_of_strings[k][index_i]:
            return False
    return True

class Solution:
    def minDeletionSize(self, list_of_strings: List[str]) -> int:
        number_of_rows = len(list_of_strings)
        if number_of_rows == 0:
            return 0
        number_of_columns = len(list_of_strings[0])
        dp = GenerateListWithMultipleElementsOfValue(number_of_columns, 1)

        for i in range(1, number_of_columns):
            for j in range(i):
                if AllCharactersNonDecreasing(list_of_strings, number_of_rows, j, i):
                    dp[i] = max(dp[i], dp[j] + 1)

        longest_non_decreasing_subsequence_length = max(dp, default=0)
        result = number_of_columns - longest_non_decreasing_subsequence_length
        return result