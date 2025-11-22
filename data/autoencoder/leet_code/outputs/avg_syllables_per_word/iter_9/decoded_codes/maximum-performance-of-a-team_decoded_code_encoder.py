import heapq

class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        engineers = sorted(zip(efficiency, speed), key=lambda x: -x[0])
        speed_heap = []
        speed_sum = 0
        max_performance = 0
        MOD = 10**9 + 7

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            speed_sum += spd

            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)

            max_performance = max(max_performance, speed_sum * eff)

        return max_performance % MOD