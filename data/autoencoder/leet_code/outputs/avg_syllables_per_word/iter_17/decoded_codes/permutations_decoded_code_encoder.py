from typing import List

class Solution:
    def permute(self, list_of_numbers: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(current_path: List[int], remaining_numbers: List[int]):
            if not remaining_numbers:
                permutations.append(current_path)
                return
            for index in range(len(remaining_numbers)):
                new_path = current_path + [remaining_numbers[index]]
                new_remaining = remaining_numbers[:index] + remaining_numbers[index+1:]
                backtrack(new_path, new_remaining)

        backtrack([], list_of_numbers)
        return permutations