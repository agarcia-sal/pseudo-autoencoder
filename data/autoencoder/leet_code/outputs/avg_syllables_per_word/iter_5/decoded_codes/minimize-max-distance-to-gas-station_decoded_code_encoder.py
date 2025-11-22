class Solution:
    def minmaxGasDist(self, stations, k):
        def possible(max_dist):
            additional_stations = 0
            for i in range(1, len(stations)):
                dist = stations[i] - stations[i - 1]
                additional_stations += int(dist // max_dist)
                if additional_stations > k:
                    return False
            return True

        left, right = 0, 1e8
        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left