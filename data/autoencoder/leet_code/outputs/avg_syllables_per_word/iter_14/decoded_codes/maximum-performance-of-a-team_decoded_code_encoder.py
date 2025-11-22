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
                speed_sum -= heapq.heappop(speed_heap)

            current_performance = speed_sum * eff
            if current_performance > max_performance:
                max_performance = current_performance

        MODULUS = 10**9 + 7
        max_performance %= MODULUS
        return max_performance