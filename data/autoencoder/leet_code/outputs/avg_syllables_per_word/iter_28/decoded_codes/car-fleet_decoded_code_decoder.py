from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_positions_and_speeds = sorted(
            zip(position, speed), key=lambda x: x[0], reverse=True
        )
        time_to_target = [
            (target - pos) / spd for pos, spd in paired_positions_and_speeds
        ]
        fleets = 0
        current_max_time = 0.0
        for time_element in time_to_target:
            if time_element > current_max_time:
                fleets += 1
                current_max_time = time_element
        return fleets