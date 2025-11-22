from typing import List

class Solution:
    def permuteUnique(self, list_of_numbers: List[int]) -> List[List[int]]:
        def backtrack(current_path: List[int], used_flags: List[bool], result_list: List[List[int]]):
            if len(current_path) == len(list_of_numbers):
                result_list.append(current_path[:])
                return
            for index in range(len(list_of_numbers)):
                if used_flags[index]:
                    continue
                if index > 0 and list_of_numbers[index] == list_of_numbers[index - 1] and not used_flags[index - 1]:
                    continue
                used_flags[index] = True
                current_path.append(list_of_numbers[index])
                backtrack(current_path, used_flags, result_list)
                current_path.pop()
                used_flags[index] = False

        list_of_numbers.sort()
        result_list = []
        used_flags = [False] * len(list_of_numbers)
        backtrack([], used_flags, result_list)
        return result_list