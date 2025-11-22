from typing import List

class Solution:
    def numRescueBoats(self, list_of_people: List[int], weight_limit: int) -> int:
        list_of_people.sort()
        left_pointer, right_pointer = 0, len(list_of_people) - 1
        boat_count = 0
        while left_pointer <= right_pointer:
            if list_of_people[left_pointer] + list_of_people[right_pointer] <= weight_limit:
                left_pointer += 1
            right_pointer -= 1
            boat_count += 1
        return boat_count