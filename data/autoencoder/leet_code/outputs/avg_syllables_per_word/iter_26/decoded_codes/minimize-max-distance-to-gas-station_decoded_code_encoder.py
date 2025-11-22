class Solution:
    def minmaxGasDist(self, stations, k):
        def possible(max_dist):
            additional_stations = 0
            for i in range(1, len(stations)):
                distance_difference = stations[i] - stations[i - 1]
                additional_stations += int(distance_difference / max_dist)
            return additional_stations <= k

        left, right = 0.0, 100_000_000.0
        while right - left > 1e-7:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left