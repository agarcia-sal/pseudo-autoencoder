from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]) -> None:
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result: List[List[int]] = []
        backtrack(0, target, [])
        return result