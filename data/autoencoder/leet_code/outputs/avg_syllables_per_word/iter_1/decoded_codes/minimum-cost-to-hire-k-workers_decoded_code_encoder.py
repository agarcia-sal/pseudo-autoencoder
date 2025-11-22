import heapq

def min_cost_to_hire_workers(workers, k):
    # Sort workers by wage/quality ratio
    workers.sort(key=lambda x: x[0] / x[1])  # assuming worker = (wage, quality)

    max_heap = []
    total_q = 0
    min_cost = float('inf')

    for wage, quality in workers:
        r = wage / quality
        heapq.heappush(max_heap, -quality)
        total_q += quality

        if len(max_heap) > k:
            total_q += heapq.heappop(max_heap)  # pop returns negative quality

        if len(max_heap) == k:
            min_cost = min(min_cost, total_q * r)

    return min_cost