from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda x: x[0], reverse=True)
        time_to_target = []
        for p, s in pairs:
            time = (target - p) / s
            time_to_target.append(time)
        fleets = 0
        current_max_time = 0
        for time in time_to_target:
            if time > current_max_time:
                fleets += 1
                current_max_time = time
        return fleets