from typing import List, Tuple

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_target: List[float] = []
        zipped_pairs: List[Tuple[int, int]] = list(zip(position, speed))
        zipped_pairs.sort(key=lambda x: x[0], reverse=True)

        for p, s in zipped_pairs:
            if s == 0:
                # If speed is zero and car is not at target, time is infinite (car never reaches target)
                time = float('inf') if p < target else 0.0
            else:
                time = (target - p) / s if p <= target else 0.0
            time_to_target.append(time)

        fleets = 0
        current_max_time = 0.0

        for t in time_to_target:
            if t > current_max_time:
                fleets += 1
                current_max_time = t

        return fleets