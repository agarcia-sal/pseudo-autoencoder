from typing import List

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(max_dist: float) -> bool:
            additional_stations = 0
            for i in range(1, len(stations)):
                distance = stations[i] - stations[i - 1]
                additional_stations += int(distance / max_dist)
            return additional_stations <= k

        left, right = 0.0, 10**8
        epsilon = 1e-6
        while right - left > epsilon:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left