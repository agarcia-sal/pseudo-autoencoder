from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)

        time_to_target = []
        for pos, spd in sorted_pairs:
            time = (target - pos) / spd
            time_to_target.append(time)

        fleets = 0
        current_max_time = 0.0
        for time in time_to_target:
            if time > current_max_time:
                fleets += 1
                current_max_time = time

        return fleets