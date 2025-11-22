class Solution:
    def minmaxGasDist(self, stations, k):
        def possible(max_dist):
            additional_stations = 0
            for i in range(1, len(stations)):
                distance = stations[i] - stations[i - 1]
                needed = int(distance / max_dist)
                additional_stations += needed
            return additional_stations <= k

        left, right = 0, 100000000
        while right - left > 0.000001:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left