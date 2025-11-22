from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_position_speed = [(pos, spd) for pos, spd in zip(position, speed)]
        sorted_pairs = sorted(paired_position_speed, key=lambda x: x[0], reverse=True)
        time_to_target = [(target - pos) / spd for pos, spd in sorted_pairs]
        fleets = 0
        current_max_time = 0.0
        for time_element in time_to_target:
            if time_element > current_max_time:
                fleets += 1
                current_max_time = time_element
        return fleets