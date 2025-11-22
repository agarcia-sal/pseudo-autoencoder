from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each position with its corresponding speed
        position_speed_pairs = list(zip(position, speed))
        # Sort the pairs by position in descending order (cars closest to the target first)
        sorted_pairs = sorted(position_speed_pairs, key=lambda x: x[0], reverse=True)

        times = []
        for pos, spd in sorted_pairs:
            time = (target - pos) / spd
            times.append(time)

        fleets = 0
        current_max_time = 0
        for time in times:
            if time > current_max_time:
                fleets += 1
                current_max_time = time

        return fleets