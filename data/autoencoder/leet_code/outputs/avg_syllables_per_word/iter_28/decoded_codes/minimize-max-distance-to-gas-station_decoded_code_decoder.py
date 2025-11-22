from typing import List

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(max_dist: float) -> bool:
            additional_stations = 0
            for i in range(1, len(stations)):
                dist = stations[i] - stations[i - 1]
                additional_stations += int(dist / max_dist)
                if additional_stations > k:
                    return False
            return True

        left, right = 0.0, 100_000_000.0
        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left