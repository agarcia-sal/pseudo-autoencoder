import heapq

def max_performance(efficiency, speed, k):
    engineers = list(zip(efficiency, speed))
    engineers.sort(key=lambda x: x[0], reverse=True)

    speed_heap = []
    speed_sum = 0
    max_perf = 0
    MOD = 10**9 + 7

    for eff, spd in engineers:
        heapq.heappush(speed_heap, spd)
        speed_sum += spd
        if len(speed_heap) > k:
            speed_sum -= heapq.heappop(speed_heap)
        max_perf = max(max_perf, speed_sum * eff)

    return max_perf % MOD