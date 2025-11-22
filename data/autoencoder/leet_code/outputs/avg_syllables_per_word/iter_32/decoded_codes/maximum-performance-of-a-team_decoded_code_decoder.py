from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7

        # Pair efficiency and speed, then sort descending by efficiency
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True, key=lambda x: x[0])

        speed_heap = []
        speed_sum = 0
        max_performance = 0

        for eff, spd in engineers:
            # Push current speed to min-heap
            heapq.heappush(speed_heap, spd)
            speed_sum += spd

            # Keep at most k engineers by removing smallest speed if needed
            if len(speed_heap) > k:
                smallest_speed = heapq.heappop(speed_heap)
                speed_sum -= smallest_speed

            current_performance = speed_sum * eff
            if current_performance > max_performance:
                max_performance = current_performance

        return max_performance % MOD