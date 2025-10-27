from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path: List[int], remaining: List[int]) -> None:
            if len(remaining) == 0:
                permutations.append(path)
                return
            for i in range(len(remaining)):
                new_path = path + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(new_path, new_remaining)

        permutations: List[List[int]] = []
        backtrack([], nums)
        return permutations