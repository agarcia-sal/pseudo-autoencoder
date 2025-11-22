import heapq

class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        engineers = []
        for i in range(n):
            engineers.append((efficiency[i], speed[i]))
        engineers.sort(key=lambda x: x[0], reverse=True)

        speed_min_heap = []
        sum_of_speeds = 0
        max_performance = 0
        MOD = 10**9 + 7

        for eff, spd in engineers:
            heapq.heappush(speed_min_heap, spd)
            sum_of_speeds += spd

            if len(speed_min_heap) > k:
                removed_speed = heapq.heappop(speed_min_heap)
                sum_of_speeds -= removed_speed

            current_performance = sum_of_speeds * eff
            if current_performance > max_performance:
                max_performance = current_performance

        return max_performance % MOD