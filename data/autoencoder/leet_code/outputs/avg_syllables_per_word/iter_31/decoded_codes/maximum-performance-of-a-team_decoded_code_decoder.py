import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers = [(efficiency[i], speed[i]) for i in range(n)]
        engineers.sort(key=lambda x: x[0], reverse=True)  # sort by efficiency descending

        speed_heap = []
        speed_sum = 0
        max_performance = 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            speed_sum += spd

            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)

            current_performance = speed_sum * eff
            if current_performance > max_performance:
                max_performance = current_performance

        return max_performance % MOD