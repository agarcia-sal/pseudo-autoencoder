from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, target: int, path: List[int]):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for index in range(start, len(candidates)):
                # pass a new list with the current candidate appended
                backtrack(index, target - candidates[index], path + [candidates[index]])

        backtrack(0, target, [])
        return result