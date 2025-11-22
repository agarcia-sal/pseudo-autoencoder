from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each position with speed, then sort descending by position
        list_of_pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        time_to_target = []
        for pos, spd in list_of_pairs:
            # Time to reach target from position at given speed
            time_needed = (target - pos) / spd
            time_to_target.append(time_needed)

        fleets = 0
        current_max_time = 0.0
        for t in time_to_target:
            if t > current_max_time:
                fleets += 1
                current_max_time = t

        return fleets