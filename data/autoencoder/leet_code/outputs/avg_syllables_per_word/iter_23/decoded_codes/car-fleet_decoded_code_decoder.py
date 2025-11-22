from typing import List, Tuple

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds and sort by position descending
        paired_sorted_position_speed: List[Tuple[int, int]] = sorted(
            zip(position, speed), key=lambda x: x[0], reverse=True
        )

        time_to_target: List[float] = []
        for p, s in paired_sorted_position_speed:
            time_for_car = (target - p) / s
            time_to_target.append(time_for_car)

        fleets: int = 0
        current_max_time: float = 0.0

        for time_element in time_to_target:
            if time_element > current_max_time:
                fleets += 1
                current_max_time = time_element

        return fleets