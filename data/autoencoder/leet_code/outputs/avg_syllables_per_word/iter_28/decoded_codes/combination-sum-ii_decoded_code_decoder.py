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
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, target_value - candidates[i], path_list + [candidates[i]])

        backtrack(0, target, [])
        return result