import math

def minmaxGasDist(stations, k):
    def possible(max_d):
        count = 0
        for i in range(1, len(stations)):
            count += math.floor((stations[i] - stations[i-1]) / max_d)
        return count <= k

    left, right = 0, 1e8
    while right - left > 1e-6:
        mid = (left + right) / 2
        if possible(mid):
            right = mid
        else:
            left = mid
    return left