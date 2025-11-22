class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(start: int, path: list[int]) -> None:
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        result: list[list[int]] = []
        backtrack(1, [])
        return result