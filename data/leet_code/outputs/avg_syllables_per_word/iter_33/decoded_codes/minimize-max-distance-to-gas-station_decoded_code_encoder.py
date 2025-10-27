class Solution:
    def minmaxGasDist(self, stations, k):
        def possible(max_dist):
            additional_stations = 0
            for i in range(1, len(stations)):
                dist = stations[i] - stations[i - 1]
                additional_stations += int(dist // max_dist)
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