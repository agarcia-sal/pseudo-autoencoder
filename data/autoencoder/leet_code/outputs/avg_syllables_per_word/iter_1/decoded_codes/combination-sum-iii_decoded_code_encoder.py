def combinationSum3(k, n):
    result = []
    def backtrack(start, path, target, k):
        if target == 0 and k == 0:
            result.append(path)
            return
        if target < 0 or k < 0:
            return
        for i in range(start, 10):
            backtrack(i + 1, path + [i], target - i, k - 1)
    backtrack(1, [], n, k)
    return result