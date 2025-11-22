class Solution:
    def permute(self, nums):
        def backtrack(path, remaining):
            if len(remaining) == 0:
                permutations.append(path)
                return
            for index in range(len(remaining)):
                new_path = path + [remaining[index]]
                new_remaining = remaining[:index] + remaining[index+1:]
                backtrack(new_path, new_remaining)
        permutations = []
        backtrack([], nums)
        return permutations