import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        # Pair each query with its index and sort by query value
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])

        min_heap = []
        result = [-1] * len(queries)

        interval_index = 0
        n = len(intervals)

        for query, original_index in sorted_queries:
            # Add all intervals starting before or at query to the heap
            while interval_index < n and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                interval_size = end - start + 1
                # Heap element: (interval_size, interval_end)
                heapq.heappush(min_heap, (interval_size, end))
                interval_index += 1

            # Remove intervals from heap which end before query (intervals that don't cover query)
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            if min_heap:
                result[original_index] = min_heap[0][0]

        return result