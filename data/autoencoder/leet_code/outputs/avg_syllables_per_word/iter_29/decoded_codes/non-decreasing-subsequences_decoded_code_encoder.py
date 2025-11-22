from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(current_index: int, last_value: int, temporary_list: List[int]) -> None:
            if current_index == n:
                if len(temporary_list) > 1:
                    ans.append(temporary_list[:])
                return

            if nums[current_index] >= last_value:
                temporary_list.append(nums[current_index])
                dfs(current_index + 1, nums[current_index], temporary_list)
                temporary_list.pop()

            # To avoid duplicates, only recurse without including current element if 
            # it is different from last_value (skip repeating the same element twice)
            if nums[current_index] != last_value:
                dfs(current_index + 1, last_value, temporary_list)

        dfs(0, -1000, [])
        return ans