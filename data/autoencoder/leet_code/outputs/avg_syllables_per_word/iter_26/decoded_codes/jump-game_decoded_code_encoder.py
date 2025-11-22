from typing import List

class Solution:
    def canJump(self, list_of_numbers: List[int]) -> bool:
        farthest_reachable_index = 0
        for index in range(len(list_of_numbers)):
            if index > farthest_reachable_index:
                return False
            possible_reach = index + list_of_numbers[index]
            if possible_reach > farthest_reachable_index:
                farthest_reachable_index = possible_reach
        return farthest_reachable_index >= len(list_of_numbers) - 1