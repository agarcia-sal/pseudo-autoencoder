from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]) -> None:
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for index in range(start, len(candidates)):
                backtrack(index, target - candidates[index], path + [candidates[index]])

        result = []
        backtrack(0, target, [])
        return result