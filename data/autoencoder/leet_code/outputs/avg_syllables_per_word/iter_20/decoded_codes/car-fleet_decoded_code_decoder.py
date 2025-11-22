from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        time_to_target = [(target - p) / s for p, s in pairs]

        fleets = 0
        current_max_time = 0.0
        for t in time_to_target:
            if t > current_max_time:
                fleets += 1
                current_max_time = t

        return fleets