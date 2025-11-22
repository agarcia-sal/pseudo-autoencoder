from typing import List

class Solution:
    def canJump(self, list_of_numbers: List[int]) -> bool:
        farthest_index_reachable = 0
        for index in range(len(list_of_numbers)):
            if index > farthest_index_reachable:
                return False
            farthest_index_reachable = max(farthest_index_reachable, index + list_of_numbers[index])
        return farthest_index_reachable >= len(list_of_numbers) - 1