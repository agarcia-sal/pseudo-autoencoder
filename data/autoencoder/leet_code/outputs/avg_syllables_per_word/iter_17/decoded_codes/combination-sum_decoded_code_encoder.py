from typing import List

class Solution:
    def combinationSum(self, list_of_candidates: List[int], target_value: int) -> List[List[int]]:
        result_collection = []

        def backtrack(start_index: int, current_target: int, current_path: List[int]) -> None:
            if current_target == 0:
                result_collection.append(current_path)
                return
            if current_target < 0:
                return
            for index in range(start_index, len(list_of_candidates)):
                backtrack(index, current_target - list_of_candidates[index], current_path + [list_of_candidates[index]])

        backtrack(0, target_value, [])
        return result_collection