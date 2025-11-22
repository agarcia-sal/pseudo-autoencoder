class Solution:
    def permute(self, nums):
        def backtrack(path, remaining):
            if not remaining:
                permutations.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        permutations = []
        backtrack([], nums)
        return permutations