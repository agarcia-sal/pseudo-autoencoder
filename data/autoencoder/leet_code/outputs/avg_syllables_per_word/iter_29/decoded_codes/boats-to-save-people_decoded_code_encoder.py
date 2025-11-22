from typing import List

class Solution:
    def numRescueBoats(self, people_list: List[int], limit_value: int) -> int:
        people_list.sort()
        left_pointer = 0
        right_pointer = len(people_list) - 1
        boat_count = 0

        while left_pointer <= right_pointer:
            if people_list[left_pointer] + people_list[right_pointer] <= limit_value:
                left_pointer += 1
            right_pointer -= 1
            boat_count += 1

        return boat_count