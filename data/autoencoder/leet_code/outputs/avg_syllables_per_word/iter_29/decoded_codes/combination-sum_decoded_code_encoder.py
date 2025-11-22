from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_collection = []

        def backtrack(start: int, target_value: int, current_path: List[int]) -> None:
            if target_value == 0:
                result_collection.append(current_path)
                return
            if target_value < 0:
                return
            for index in range(start, len(candidates)):
                backtrack(index, target_value - candidates[index], current_path + [candidates[index]])

        backtrack(0, target, [])
        return result_collection