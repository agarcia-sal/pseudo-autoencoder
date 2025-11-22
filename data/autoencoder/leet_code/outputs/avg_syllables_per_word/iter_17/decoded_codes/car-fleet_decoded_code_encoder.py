from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_list = list(zip(position, speed))
        sorted_pairs = sorted(paired_list, reverse=True)
        time_to_target = []
        for pos, spd in sorted_pairs:
            time_value = (target - pos) / spd
            time_to_target.append(time_value)

        fleets = 0
        current_max_time = 0
        for time in time_to_target:
            if time > current_max_time:
                fleets += 1
                current_max_time = time

        return fleets