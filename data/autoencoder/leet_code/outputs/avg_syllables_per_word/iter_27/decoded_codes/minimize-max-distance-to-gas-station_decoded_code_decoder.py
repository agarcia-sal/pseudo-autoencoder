from typing import List

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(max_dist: float) -> bool:
            additional_stations = 0
            for i in range(1, len(stations)):
                distance_between_stations = stations[i] - stations[i - 1]
                additional_needed = distance_between_stations / max_dist
                additional_stations += int(additional_needed)
                if additional_stations > k:
                    return False
            return additional_stations <= k

        left, right = 0.0, 100_000_000.0
        EPS = 1e-6
        while right - left > EPS:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left