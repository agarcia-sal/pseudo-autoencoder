from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], target: int, k_remaining: int):
            if target == 0 and k_remaining == 0:
                result.append(path[:])
                return
            if target < 0 or k_remaining < 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, target - i, k_remaining - 1)
                path.pop()

        backtrack(1, [], n, k)
        return result