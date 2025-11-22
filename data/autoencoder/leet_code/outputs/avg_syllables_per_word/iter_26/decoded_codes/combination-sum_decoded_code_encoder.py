from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, target_value: int, path_list: List[int]) -> None:
            if target_value == 0:
                result.append(path_list)
                return
            if target_value < 0:
                return
            for index in range(start, len(candidates)):
                backtrack(index, target_value - candidates[index], path_list + [candidates[index]])

        backtrack(0, target, [])
        return result