class Solution:
    def minmaxGasDist(self, stations, k):
        def possible(max_dist):
            additional_stations = 0
            for i in range(1, len(stations)):
                distance = stations[i] - stations[i - 1]
                additional_stations += int(distance // max_dist)
            return additional_stations <= k

        left = 0
        right = 100000000

        while right - left > 0.000001:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left