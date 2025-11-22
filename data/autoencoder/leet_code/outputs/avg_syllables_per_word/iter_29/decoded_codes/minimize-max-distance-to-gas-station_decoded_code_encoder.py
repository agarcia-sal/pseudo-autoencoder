class Solution:
    def minmaxGasDist(self, stations, k):
        def possible(max_dist):
            additional_stations = 0
            for i in range(1, len(stations)):
                distance = stations[i] - stations[i - 1]
                # Stations needed is how many intervals of max_dist fit in distance minus one
                additional_stations += int(distance // max_dist)
            return additional_stations <= k

        left, right = 0.0, 10**8
        eps = 1e-6  # precision threshold

        while right - left > eps:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid

        return left