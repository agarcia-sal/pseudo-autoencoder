from typing import List

class Solution:
    def subsets(self, list_of_numbers: List[int]) -> List[List[int]]:
        if len(list_of_numbers) == 0:
            return [[]]
        subsets_without_first = self.subsets(list_of_numbers[1:])
        subsets_with_first = []
        for subset in subsets_without_first:
            new_subset = [list_of_numbers[0]] + subset
            subsets_with_first.append(new_subset)
        return subsets_without_first + subsets_with_first