from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start: int, target_remaining: int, path: List[int]) -> None:
            if target_remaining == 0:
                result.append(path)
                return
            if target_remaining < 0:
                return
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue
                backtrack(index + 1, target_remaining - candidates[index], path + [candidates[index]])

        backtrack(0, target, [])
        return result