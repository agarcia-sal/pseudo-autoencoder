class Solution:
    def permute(self, nums):
        def backtrack(path, remaining):
            if not remaining:
                permutations.append(path)
                return
            for i in range(len(remaining)):
                new_path = path + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(new_path, new_remaining)

        permutations = []
        backtrack([], nums)
        return permutations