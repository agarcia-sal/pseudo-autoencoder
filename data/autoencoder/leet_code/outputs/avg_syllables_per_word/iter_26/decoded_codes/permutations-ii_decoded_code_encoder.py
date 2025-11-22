from typing import List

class Solution:
    def permuteUnique(self, list_of_numbers: List[int]) -> List[List[int]]:
        def backtrack(current_path: List[int], list_of_used_flags: List[bool], list_of_results: List[List[int]]):
            if len(current_path) == len(list_of_numbers):
                list_of_results.append(current_path[:])
                return

            for index in range(len(list_of_numbers)):
                if list_of_used_flags[index]:
                    continue
                if index > 0 and list_of_numbers[index] == list_of_numbers[index - 1] and not list_of_used_flags[index - 1]:
                    continue

                list_of_used_flags[index] = True
                current_path.append(list_of_numbers[index])
                backtrack(current_path, list_of_used_flags, list_of_results)
                current_path.pop()
                list_of_used_flags[index] = False

        list_of_numbers.sort()
        list_of_results = []
        list_of_used_flags = [False] * len(list_of_numbers)
        backtrack([], list_of_used_flags, list_of_results)
        return list_of_results