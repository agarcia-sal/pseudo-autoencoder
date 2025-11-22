from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target_value: int, path: List[int]) -> None:
            if target_value == 0:
                result.append(path)
                return
            if target_value < 0:
                return
            for index in range(start, len(candidates)):
                backtrack(index, target_value - candidates[index], path + [candidates[index]])

        result = []
        backtrack(0, target, [])
        return result