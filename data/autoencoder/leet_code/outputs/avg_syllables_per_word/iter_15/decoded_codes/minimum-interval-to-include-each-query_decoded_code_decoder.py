import heapq
from typing import List, Tuple

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start time ascending
        intervals.sort(key=lambda x: x[0])
        # Pair queries with their original indices and sort by query value ascending
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])
        min_heap: List[Tuple[int, int]] = []  # stores pairs of (interval_size, interval_end)
        result = [-1] * len(queries)
        interval_index = 0
        n = len(intervals)

        for query, original_index in sorted_queries:
            # Push all intervals starting before or at the query into the heap
            while interval_index < n and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                interval_size = end - start + 1
                heapq.heappush(min_heap, (interval_size, end))
                interval_index += 1
            # Remove intervals from heap whose end is less than the query because they don't contain query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            if min_heap:
                result[original_index] = min_heap[0][0]

        return result