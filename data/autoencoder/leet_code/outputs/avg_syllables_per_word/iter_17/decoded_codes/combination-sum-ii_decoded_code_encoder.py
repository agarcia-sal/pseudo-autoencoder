from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start: int, target_value: int, path_list: List[int]) -> None:
            if target_value == 0:
                result.append(path_list)
                return
            if target_value < 0:
                return
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue
                backtrack(index + 1, target_value - candidates[index], path_list + [candidates[index]])

        backtrack(0, target, [])
        return result