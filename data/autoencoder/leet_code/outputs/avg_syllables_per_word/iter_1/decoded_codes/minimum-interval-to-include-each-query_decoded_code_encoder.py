import heapq

def find_min_interval(intervals, queries):
    intervals.sort(key=lambda x: x[0])
    sorted_q = sorted([(q, i) for i, q in enumerate(queries)])
    heap = []
    res = [-1] * len(queries)
    i = 0
    for q, idx in sorted_q:
        while i < len(intervals) and intervals[i][0] <= q:
            length = intervals[i][1] - intervals[i][0] + 1
            heapq.heappush(heap, (length, intervals[i][1]))
            i += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        if heap:
            res[idx] = heap[0][0]
    return res