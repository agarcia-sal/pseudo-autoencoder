import heapq
from typing import List, Tuple

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their start value
        intervals.sort(key=lambda x: x[0])
        # Sort queries along with original indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        min_heap = []  # heap will store pairs of (interval_size, interval_end)
        result = [-1] * len(queries)
        interval_index = 0
        n = len(intervals)

        for query, original_index in sorted_queries:
            # Add all intervals starting <= query
            while interval_index < n and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                interval_size = end - start + 1
                heapq.heappush(min_heap, (interval_size, end))
                interval_index += 1

            # Remove intervals that end before query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # The smallest interval containing query is at the top of the heap if exists
            if min_heap:
                result[original_index] = min_heap[0][0]

        return result