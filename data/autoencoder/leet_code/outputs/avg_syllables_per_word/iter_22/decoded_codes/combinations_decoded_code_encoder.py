from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, path: List[int]) -> None:
            if len(path) == k:
                result.append(path[:])  # Append a copy of path
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        result: List[List[int]] = []
        backtrack(1, [])
        return result