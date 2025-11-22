from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_length = 0

        for i in range(len(nums)):
            if not visited[i]:
                current_length = 0
                k = i
                while not visited[k]:
                    visited[k] = True
                    k = nums[k]
                    current_length += 1
                max_length = max(max_length, current_length)

        return max_length