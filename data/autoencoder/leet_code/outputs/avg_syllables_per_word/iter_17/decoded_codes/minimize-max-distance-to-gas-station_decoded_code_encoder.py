class Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        def possible(max_dist: float) -> bool:
            additional_stations = 0
            for i in range(1, len(stations)):
                distance_difference = stations[i] - stations[i - 1]
                stations_needed = int(distance_difference // max_dist)
                additional_stations += stations_needed
            return additional_stations <= k

        left, right = 0.0, 10**8  # 100_000_000 as in pseudocode

        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid

        return left