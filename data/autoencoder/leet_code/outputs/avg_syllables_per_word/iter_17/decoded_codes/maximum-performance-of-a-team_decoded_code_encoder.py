import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)  # sort by efficiency descending

        min_heap = []
        sum_speeds = 0
        max_perf = 0
        MOD = 10**9 + 7

        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)
            sum_speeds += spd

            if len(min_heap) > k:
                removed_speed = heapq.heappop(min_heap)
                sum_speeds -= removed_speed

            current_perf = sum_speeds * eff
            if current_perf > max_perf:
                max_perf = current_perf

        return max_perf % MOD