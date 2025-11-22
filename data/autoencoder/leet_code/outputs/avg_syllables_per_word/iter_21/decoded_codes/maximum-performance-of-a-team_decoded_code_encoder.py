import heapq

class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        # Pair engineers by efficiency descending order
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        speed_sum = 0
        max_performance = 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            speed_sum += spd

            if len(speed_heap) > k:
                removed_speed = heapq.heappop(speed_heap)
                speed_sum -= removed_speed

            current_performance = speed_sum * eff
            if current_performance > max_performance:
                max_performance = current_performance

        modulus_base = 10**9 + 7
        return max_performance % modulus_base