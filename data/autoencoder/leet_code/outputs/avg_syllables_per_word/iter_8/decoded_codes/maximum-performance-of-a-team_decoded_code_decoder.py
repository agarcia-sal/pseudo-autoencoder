import heapq

class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        engineers = list(zip(efficiency, speed))
        engineers.sort(key=lambda x: x[0], reverse=True)

        speed_heap = []
        speed_sum = 0
        max_performance = 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            speed_sum += spd

            if len(speed_heap) > k:
                removed = heapq.heappop(speed_heap)
                speed_sum -= removed

            current_performance = speed_sum * eff
            if current_performance > max_performance:
                max_performance = current_performance

        return max_performance % (10**9 + 7)