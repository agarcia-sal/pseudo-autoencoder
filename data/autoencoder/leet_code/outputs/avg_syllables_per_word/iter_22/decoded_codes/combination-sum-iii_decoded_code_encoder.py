class Solution:
    def combinationSum3(self, k: int, n: int):
        def backtrack(start, path, target, k):
            if target == 0 and k == 0:
                result.append(path.copy())
                return
            if target < 0 or k < 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, target - i, k - 1)
                path.pop()

        result = []
        backtrack(1, [], n, k)
        return result