from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path: List[int], remaining: List[int]) -> None:
            if not remaining:
                permutations.append(path)
                return
            for index in range(len(remaining)):
                new_path = path + [remaining[index]]
                new_remaining = remaining[:index] + remaining[index+1:]
                backtrack(new_path, new_remaining)

        permutations = []
        backtrack([], nums)
        return permutations