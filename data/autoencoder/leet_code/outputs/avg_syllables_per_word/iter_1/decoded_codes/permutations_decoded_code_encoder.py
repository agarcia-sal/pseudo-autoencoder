def permute(nums):
    def backtrack(path, rem):
        if not rem:
            permutations.append(path)
            return
        for i in range(len(rem)):
            backtrack(path + [rem[i]], rem[:i] + rem[i+1:])
    permutations = []
    backtrack([], nums)
    return permutations