from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        time_to_target = [(target - pos) / spd for pos, spd in cars]

        fleets = 0
        current_max_time = 0.0

        for time in time_to_target:
            if time > current_max_time:
                fleets += 1
                current_max_time = time

        return fleets